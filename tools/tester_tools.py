import subprocess

def run_tests():
    try:
        result = subprocess.run(["pytest"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
