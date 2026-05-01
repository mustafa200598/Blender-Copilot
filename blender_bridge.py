import bpy
import os

# ⚠️ قم بتغيير هذا المسار إلى المسار الخاص بك على جهازك
# ⚠️ Change this path to your actual local path where blender_cmd.py is located
COMMAND_FILE = r"C:\path\to\your\project\blender_cmd.py"

# إنشاء الملف أو تفريغه عند بدء التشغيل
# Create or clear the command file on startup
with open(COMMAND_FILE, 'w', encoding='utf-8') as f:
    f.write("")

def check_commands():
    if os.path.exists(COMMAND_FILE):
        try:
            with open(COMMAND_FILE, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # إذا كان الملف يحتوي على كود جديد، قم بتنفيذه
            if code.strip() != "":
                try:
                    # Execute the code inside Blender's context
                    exec(code, globals())
                except Exception as e:
                    print(f"Error executing command: {e}")
                
                # مسح محتوى الملف بعد التنفيذ لتجنب تكرار الأمر
                # Clear the file after execution so it doesn't run again
                with open(COMMAND_FILE, 'w', encoding='utf-8') as f:
                    f.write("")
        except PermissionError:
            # File might be currently written to by the AI agent
            pass
    
    return 1.0  # Check again every 1 second / تحقق كل ثانية

# تسجيل المؤقت ليعمل في الخلفية
# Register the background timer
if not bpy.app.timers.is_registered(check_commands):
    bpy.app.timers.register(check_commands)

print("Blender AI Bridge Started! Waiting for commands...")
