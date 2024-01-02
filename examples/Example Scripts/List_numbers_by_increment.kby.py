import machine, kooka
import fonts

list_of_numbers = None
increment = None
i = None

def upRange(start, stop, step):
    while start <= stop:
        yield start
        start += abs(step)



# On-start code, run once at start-up.
if True:
    list_of_numbers = []
    increment = 3
    kooka.display.setfont(fonts.mono6x7)
    kooka.display.print('Numbers by', increment, show=0)
    for i in upRange(1, 100, float(increment)):
        list_of_numbers.append("{:1d}".format(round(i)))
    kooka.display.print(','.join(list_of_numbers), show=0)

# Main loop code, run continuously.
while True:
    kooka.display.show()
    machine.idle()

# Generated Blockly XML follows
# <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="n;:h%g,1L46tw9Xc6h/j">list_of_numbers</variable><variable id=",6*f[~n9Tj-u(Ov^Y(Sl">increment</variable><variable id="kjm~VMLRVUBB#J{fxU6s">i</variable></variables><block type="event_on_start" id="4/yjk^1hgOmY5XZGGatd" x="90" y="-150"><statement name="DO"><block type="variables_set" id="j./=V^9:$gqt`:@GC,V-"><field name="VAR" id="n;:h%g,1L46tw9Xc6h/j">list_of_numbers</field><value name="VALUE"><block type="lists_create_with" id="cQ++Q6lh*Lf79!gfE}L="><mutation items="0"></mutation></block></value><next><block type="variables_set" id=".uA@=XeGTf,U0,OFm,Md"><field name="VAR" id=",6*f[~n9Tj-u(Ov^Y(Sl">increment</field><value name="VALUE"><block type="math_number" id="}E9@:0IHzfvi,,rU$o:o"><field name="NUM">3</field></block></value><next><block type="display_setfont" id="Jl#822m:7Rmi1aso#4wM"><field name="FONT">mono6x7</field><next><block type="display_print2" id="gK`4zU#c6mBSUY}~@C[f"><value name="VALUE1"><shadow type="text" id="7|iFmx%dRi9$,hW7Yw_n"><field name="TEXT">Numbers by</field></shadow></value><value name="VALUE2"><shadow type="math_number" id="}XTvo@QQdow~|;ain~9R"><field name="NUM">123</field></shadow><block type="variables_get" id="wRB4EeF%$=_x[0q%U;#a"><field name="VAR" id=",6*f[~n9Tj-u(Ov^Y(Sl">increment</field></block></value><next><block type="controls_for" id="%CU/|?1^NVWKz3eCP5+M"><field name="VAR" id="kjm~VMLRVUBB#J{fxU6s">i</field><value name="FROM"><block type="math_number" id="*HKZK2*`;zH1|6izw*(5"><field name="NUM">1</field></block></value><value name="TO"><block type="math_number" id="KPKVF]Y{GgK*`!e1+`vE"><field name="NUM">100</field></block></value><value name="BY"><block type="variables_get" id="Ne,5q*D9}Cq]Cd`5~RK1"><field name="VAR" id=",6*f[~n9Tj-u(Ov^Y(Sl">increment</field></block></value><statement name="DO"><block type="lists_setIndex" id="0TjY){c1,|)aZUPKQ{I4"><mutation at="false"></mutation><field name="MODE">INSERT</field><field name="WHERE">LAST</field><value name="LIST"><block type="variables_get" id="9z`4f!9:%beZ~3d{+^2S"><field name="VAR" id="n;:h%g,1L46tw9Xc6h/j">list_of_numbers</field></block></value><value name="TO"><block type="str_format_int" id="]0yyS?S+hC(DJ8,@p3%c"><field name="W">1</field><value name="VALUE"><block type="variables_get" id="0-p)YvYP.F1LjC6TJi)x"><field name="VAR" id="kjm~VMLRVUBB#J{fxU6s">i</field></block></value></block></value></block></statement><next><block type="display_print" id="EP76SI4bhtu#g.2Xn]$C"><value name="VALUE"><shadow type="text" id="OqIx=?mQHs%C:Y6S48ly"><field name="TEXT">List Numbers</field></shadow><block type="lists_split" id="t~VK|bW[Ig#O8S3SZi#1"><mutation mode="JOIN"></mutation><field name="MODE">JOIN</field><value name="INPUT"><block type="variables_get" id="J=qfg5H7-zSY#tGLk.8("><field name="VAR" id="n;:h%g,1L46tw9Xc6h/j">list_of_numbers</field></block></value><value name="DELIM"><shadow type="text" id="M20fXBc3(m1M7,STaXC2"><field name="TEXT">,</field></shadow></value></block></value></block></next></block></next></block></next></block></next></block></next></block></statement></block></xml>
