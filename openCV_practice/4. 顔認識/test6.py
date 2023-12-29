import cv2

# VideoCapture オブジェクトを生成して動画を読み込む
cap = cv2.VideoCapture(0)

num = 1

while True:
    # 動画から1フレーム読み込む
    ret, frame = cap.read()
    # フレームを表示
    cv2.imshow("video", frame)

    # 's'を押したら
    if cv2.waitKey(10) & 0xFF == ord('s'):
        # いまの画面を保存
        cv2.imwrite(f"video_picture{num}.png", frame)
        print(f"success to save video_picture{num}.png")
        num += 1
    # 'q'を押したら終了
    elif cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

