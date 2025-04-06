import os
import sys
from PIL import Image

# --- تنظیمات ---
ROOT_FOLDER = r"E:\Orbit Ai\Clients\Nomer\Photography\version3"
OUTPUT_SUFFIX = "_800x800"
CANVAS_SIZE = (800, 800)
CANVAS_BG_COLOR = 'white'
SUPPORTED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
# --- پایان تنظیمات ---

def process_image(image_path, output_folder):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')

        original_width, original_height = img.size

        if original_width == 0 or original_height == 0:
             #print(f"    خطا: ابعاد نامعتبر برای تصویر '{os.path.basename(image_path)}'") # Keep error prints
             return

        if original_width >= original_height:
            target_width = CANVAS_SIZE[0]
            scale_ratio = target_width / original_width
            target_height = int(original_height * scale_ratio)
        else:
            target_height = CANVAS_SIZE[1]
            scale_ratio = target_height / original_height
            target_width = int(original_width * scale_ratio)

        target_width = max(1, target_width)
        target_height = max(1, target_height)

        try:
            resample_filter = Image.Resampling.LANCZOS
        except AttributeError:
            try:
                 resample_filter = Image.LANCZOS
            except AttributeError:
                 resample_filter = Image.ANTIALIAS

        resized_img = img.resize((target_width, target_height), resample_filter)

        canvas = Image.new('RGB', CANVAS_SIZE, CANVAS_BG_COLOR)

        paste_x = (CANVAS_SIZE[0] - target_width) // 2
        paste_y = (CANVAS_SIZE[1] - target_height) // 2

        canvas.paste(resized_img, (paste_x, paste_y))

        base_filename = os.path.basename(image_path)
        filename_without_ext, _ = os.path.splitext(base_filename)
        output_filename = f"{filename_without_ext}.jpg"
        output_path = os.path.join(output_folder, output_filename)

        canvas.save(output_path, 'JPEG', quality=95)

    except FileNotFoundError:
        print(f"    خطا: فایل پیدا نشد '{image_path}'")
    except Exception as e:
        print(f"    خطا در پردازش تصویر '{os.path.basename(image_path)}': {e}")


def main():
    if not os.path.isdir(ROOT_FOLDER):
        print(f"خطا: فولدر ریشه یافت نشد: '{ROOT_FOLDER}'")
        return

    print(f"شروع پردازش در فولدر: {ROOT_FOLDER}")
    print("-" * 30)

    total_images_processed = 0
    subfolders_found = 0

    try:
        for item_name in os.listdir(ROOT_FOLDER):
            item_path = os.path.join(ROOT_FOLDER, item_name)

            if os.path.isdir(item_path) and not item_name.endswith(OUTPUT_SUFFIX):
                subfolders_found += 1
                source_subfolder_path = item_path
                subfolder_name = item_name

                output_folder_name = f"{subfolder_name}{OUTPUT_SUFFIX}"
                output_folder_path = os.path.join(ROOT_FOLDER, output_folder_name)

                print(f"-> پردازش فولدر منبع: '{subfolder_name}'")
                print(f"   ایجاد/استفاده از فولدر خروجی: '{output_folder_name}'")

                try:
                    os.makedirs(output_folder_path, exist_ok=True)
                except OSError as e:
                    print(f"   خطا: امکان ساخت فولدر خروجی وجود ندارد '{output_folder_path}': {e}")
                    continue

                images_in_subfolder = 0
                try:
                    for filename in os.listdir(source_subfolder_path):
                        if filename.lower().endswith(SUPPORTED_EXTENSIONS):
                            source_image_path = os.path.join(source_subfolder_path, filename)
                            if os.path.isfile(source_image_path):
                                process_image(source_image_path, output_folder_path)
                                images_in_subfolder += 1

                except FileNotFoundError:
                     print(f"   خطا: زیرفولدر '{source_subfolder_path}' در حین خواندن فایل‌ها پیدا نشد.")
                except Exception as e:
                     print(f"   خطای غیرمنتظره در پردازش فایل‌های زیرفولدر '{subfolder_name}': {e}")

                if images_in_subfolder > 0:
                    print(f"   {images_in_subfolder} تصویر پردازش و در '{output_folder_name}' ذخیره شد.")
                    total_images_processed += images_in_subfolder
                else:
                    print("   هیچ تصویر معتبری در این فولدر یافت نشد.")
                print("-" * 30)

    except FileNotFoundError:
         print(f"خطا: دسترسی به فولدر ریشه '{ROOT_FOLDER}' ممکن نیست.")
         return
    except Exception as e:
         print(f"خطای غیرمنتظره در سطح فولدر ریشه: {e}")
         return

    if subfolders_found == 0:
         print(f"\nهیچ زیرفولدری (که به '{OUTPUT_SUFFIX}' ختم نشود) برای پردازش در '{ROOT_FOLDER}' یافت نشد.")
    else:
         print(f"\nپردازش کامل شد.")
         print(f"{subfolders_found} زیرفولدر منبع بررسی شد.")
         print(f"{total_images_processed} تصویر در کل پردازش و ذخیره شد.")

if __name__ == "__main__":
    main()