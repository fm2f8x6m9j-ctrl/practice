from plyer import notification
import time

# しきい値の設定（例：5秒）
threshold = 5

print(f"{threshold}秒後に通知を送ります...")
time.sleep(threshold)

notification.notify(
    title="学習の進捗",
    message="5秒経過しました！Gitのプッシュも忘れずに！",
    app_name="My Study App"
)