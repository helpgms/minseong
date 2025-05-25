import time
import os
from pathlib import Path

WATCH_DIR = Path.home() / "Pictures"
SUPPORTED_EXT = {".jpg", ".png", ".jpeg"}
AUTO_BACKUP = True 

def detect_new_photos(watch_dir):
    before = set(watch_dir.glob("*"))
    time.sleep(5)
    after = set(watch_dir.glob("*"))
    return [f for f in after - before if f.suffix.lower() in SUPPORTED_EXT]

def upload_to_cloud(photo_path):
    print(f"[Cloud] Uploading {photo_path.name}...")
    time.sleep(1)
    print(f"[Cloud] {photo_path.name} uploaded successfully.")

def main():
    print("Google Photos 자동 백업 시뮬레이션")
    new_photos = detect_new_photos(WATCH_DIR)
    if not new_photos:
        print("새로운 사진이 없습니다.")
        return

    for photo in new_photos:
        print(f"[App] Detected new photo: {photo.name}")
        if AUTO_BACKUP:
            upload_to_cloud(photo)
            print(f"[App] {photo.name} 백업 완료")
        else:
            ans = input(f"백업하시겠습니까? (y/n): ").strip().lower()
            if ans == 'y':
                upload_to_cloud(photo)
                print(f"[App] {photo.name} 백업 완료")
            else:
                print(f"[App] {photo.name} 백업 취소")
                
if __name__ == "__main__":
    main()
