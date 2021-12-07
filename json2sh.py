import json
import sys
import os

def main():
    with open('sample.json') as f:
        data = json.load(f)

    env = data['ciTests']['linux'][0]['env']
    steps = data['ciTests']['linux'][0]['steps']
    
    pre = ["conda deactivate"]
    cmd = pre + env + steps
    output = "unit_test.sh"
    with open(output, "w") as f:
        res = "\n".join(cmd)
        f.write(res)
    os.system("chmod 777 "+output)
    
    print("Output {}".format(output))

if __name__=="__main__":
    main()
