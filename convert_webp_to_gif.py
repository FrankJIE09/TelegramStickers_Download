import os
import imageio


def convert_webp_to_gif(input_path, output_path, total_duration=2.0):
    """将单个 .webp 文件转换为 .gif 文件，并动态调整帧率和持续时间"""
    images = imageio.mimread(input_path)

    # 计算缩小比例，以 3 倍为基础，确保至少有 1 帧
    reduction_factor = max(1, len(images) // 3)
    reduced_images = images[::reduction_factor]

    # 动态调整 duration，确保总时长为 total_duration
    frame_duration = total_duration / len(reduced_images)

    # 保存为 .gif 文件
    imageio.mimsave(output_path, reduced_images, format='GIF', duration=frame_duration)


def convert_folder_webps_to_gifs(input_folder, output_folder, total_duration=2.0):
    """将文件夹中的所有 .webp 文件转换为 .gif，并保存到新的文件夹中"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_filename = filename.replace('.webp', '.gif')
            output_path = os.path.join(output_folder, output_filename)
            convert_webp_to_gif(input_path, output_path, total_duration)

    print(f"All .webp files have been converted and saved to {output_folder}.")


# 使用示例
input_folder = 'niubiuniu_by_WuMingv2Bot'
output_folder = 'niubiuniu_by_WuMingv2Bot_gifs'

convert_folder_webps_to_gifs(input_folder, output_folder, total_duration=2.0)
