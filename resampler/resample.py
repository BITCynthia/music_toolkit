from pydub import AudioSegment

def resample_audio(input_file, output_file, new_sample_rate, new_bitrate):
    # 加载音频文件
    audio = AudioSegment.from_file(input_file)
    
    # 重采样音频到新的采样率
    resampled_audio = audio.set_frame_rate(new_sample_rate)
    
    # 导出重采样后的音频到新文件，并设置比特率
    resampled_audio.export(output_file, format="mp3", bitrate=new_bitrate)

# 示例用法
input_file = "audio/srv_demo.mp3"
output_file = "output/srv_demo_resampled.mp3"
new_sample_rate = 44100  # 新的采样率，单位为Hz (44.1 kHz)
new_bitrate = "320k"  # 新的比特率 (320 kbps)

resample_audio(input_file, output_file, new_sample_rate, new_bitrate)
print(f"音频已重采样到 {new_sample_rate} Hz 和 {new_bitrate} 比特率，并保存为 {output_file}。")
