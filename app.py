import gradio as gr
from ultralytics import YOLO
import cv2
import numpy as np
import torch  # 添加torch导入

# 加载训练好的模型
model = YOLO("./student_behaviour/train_v2/weights/best.pt")

def predict_image(img):
    # 确保图像是numpy数组
    if isinstance(img, np.ndarray):
        img_cv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    else:
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # 执行预测
    results = model.predict(
        img_cv, 
        conf=0.5,
        imgsz=640,
        device='cuda:0' if torch.cuda.is_available() else 'cpu'
    )
    
    # 绘制结果
    res_img = results[0].plot()
    res_img = cv2.cvtColor(res_img, cv2.COLOR_BGR2RGB)  # 确保转换为RGB
    
    # 收集检测结果
    detections = []
    for box in results[0].boxes:
        class_id = int(box.cls)
        class_name = model.names[class_id]
        confidence = float(box.conf)
        detections.append(f"{class_name}: {confidence:.2f}")
    
    return res_img, "\n".join(detections) if detections else "未检测到行为"

# 创建Gradio界面
with gr.Blocks(theme=gr.themes.Soft(), title="学生行为检测系统") as demo:
    gr.Markdown("# 🎓 学生课堂行为检测系统")
    
    with gr.Row():
        image_input = gr.Image(label="上传课堂照片", type="numpy")
        image_output = gr.Image(label="检测结果")
    
    text_output = gr.Textbox(label="检测到的行为")
    
    submit_btn = gr.Button("开始检测", variant="primary")
    
    # 添加示例图片
    gr.Examples(
        examples=["example1.jpeg", "example2.jpeg"],
        inputs=image_input,
        outputs=[image_output, text_output],
        fn=predict_image,
        cache_examples=True
    )
    
    submit_btn.click(
        predict_image,
        inputs=image_input,
        outputs=[image_output, text_output]
    )

if __name__ == "__main__":
    # 使用明确的本地地址
    demo.launch(
        server_name="127.0.0.1",  # 使用明确的本地地址
        server_port=7860,
        share=False,
        show_error=True
    )