from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)
VMs = ['NY-VPC-PRIS01', 'NY-VPC-PRIS02', 'NY-VPC-PRIS03', 'NY-VPC-PRIS04', 'NY-VPC-PRIS07', 'NY-VPC-PRIS08',
       'NY-VPC-PRIS09', 'NY-VPC-PRIS10', 'NY-VPC-PRIS11', 'NY-VPC-PRIS12', 'NY-VPC-PRIS13', 'NY-VPC-PRIS14',
       'NY-VPC-PRIS15', 'NY-VPC-PRIS16', 'NY-VPC-PRIS17', 'NY-VPC-PRIS18', 'NY-VPC-PRIS23', 'NY-VPC-PRIS24',
       'NY-VPC-PRIS25', 'NY-VPC-PRIS26', 'NY-VPC-PRIS27']

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/render_start')
def render_start():
    return render_template('start.html',vm=VMs)

@app.route('/startall', methods=['POST'])
def startall():
    vm_nodes = ""
    for i in VMs:
        vm_nodes += """\\\\""" + i + ' '
    # print(vm_nodes)
    query = "Psexec.exe " + vm_nodes + "-accepteula -u DDS-NA\qaadmin -p qatest -s -i 2 -d \\\\ny-vpc-sgrid.na.rtdom.net\GRID_BINARIES\starttemp.bat"
    print(query)
    # os.system(query)
    return redirect(url_for('render_start'))

@app.route('/start', methods=['POST'])
def start():
    y=request.form.getlist('check')
    vm_nodes = ""
    for i in y:
        vm_nodes += """\\\\""" + i + ' '
    print(vm_nodes)
    query = "Psexec.exe " + vm_nodes + "-accepteula -u DDS-NA\qaadmin -p qatest -s -i 2 -d \\\\ny-vpc-sgrid.na.rtdom.net\GRID_BINARIES\starttemp.bat"
    print(query)
    #os.system(query)
    return redirect(url_for('render_start'))


@app.route('/render_stop')
def render_stop():
    return render_template('stop.html',vm=VMs)

@app.route('/stopall', methods=['POST'])
def stopall():
    vm_nodes = ""
    for i in VMs:
        vm_nodes += """\\\\""" + i + ' '
    #print(vm_nodes)
    query = "Psexec.exe " + vm_nodes + "-accepteula -u DDS-NA\qaadmin -p qatest cmd /c \\\\ny-vpc-sgrid.na.rtdom.net\GRID_BINARIES\StopNode.bat"
    print(query)
    #os.system(query)
    return redirect(url_for('render_stop'))

@app.route('/stop', methods=['POST'])
def stop():
    y=request.form.getlist('check')
    vm_nodes = ""
    for i in y:
        vm_nodes += """\\\\""" + i + ' '
    print(vm_nodes)
    query="Psexec.exe " + vm_nodes + "-accepteula -u DDS-NA\qaadmin -p qatest cmd /c \\\\ny-vpc-sgrid.na.rtdom.net\GRID_BINARIES\StopNode.bat"
    print(query)
    os.system(query)
    return redirect(url_for('render_stop'))

if __name__ == '__main__':
    app.run()
