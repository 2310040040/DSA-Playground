from flask import Flask,render_template,request
import subprocess,os

app=Flask(__name__)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    problems={
        "arrays":["two_sum","reverse_array","max_subarray"],
         "strings":["palindrome","anagram"],
         "sliding_window":["max_sum_k","longest_unique_substring"]
    }
    return render_template("index.html",problems=problems)

@app.route("/run/<topic>/<name>",methods=["GET","POST"])
def run_code(topic,name):
    path=os.path.join(BASE_DIR,"dsa",topic,f"{name}.py")

    desc=""
    try:
        with open(path,"r",encoding="utf-8") as f:
            data=f.read()
            if data.startswith('"""'):
                desc=data.split('"""')[1].strip()
    except Exception as e:
        desc=f"Error reading description: {e}"

    output=""
    user_input=""

    if request.method=="POST":
        user_input=request.form.get("user_input","")
        r=subprocess.run(
            ["python",path,user_input],
            capture_output=True,
            text=True
        )
        output=r.stdout if r.stdout else r.stderr

    return render_template(
        "output.html",
        name=name,
        desc=desc,
        output=output,
        user_input=user_input
    )

if __name__=="__main__":
    app.run()
