from ultralytics import YOLO
import os

def main():
    # 使用现有的YAML配置文件
    config_path = r"C:\Users\Ong Yee Torng\anaconda3\envs\StudentActionDetection\dataset\dataset_increament\data.yaml"

    # 检查配置文件是否存在
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件不存在: {config_path}")

    print(f"使用配置文件: {config_path}")

    # 载YOLOv8模型
    model = YOLO(r"student_behaviour/train_v1/weights/best.pt")   # 使用预训练模型

    # 训练配置
    results = model.train(
        data=config_path,  # 直接使用现有配置文件
        epochs=20,
        imgsz=640,
        batch=4,
        device="0",  # 使用GPU
        project="student_behaviour",
        name="train_v3",
        save_period=5,
        exist_ok=True,  # 允许覆盖现有项目
        patience=5,    # 如果10个epoch验证指标没有改进则早停
        lr0=1e-5,       # 初始学习率
        lrf=0.01,       # 最终学习率 = lr0 * lrf
        optimizer="auto"
    )

    # 验证模型
    metrics = model.val()
    print(f"mAP50-95: {metrics.box.map} | mAP50: {metrics.box.map50}")

if __name__ == "__main__":
    main()
