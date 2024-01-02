import machine, kooka
import fonts

filename = None
f = None
line = None



# On-start code, run once at start-up.
if True:
    # Open the text file for reading
    filename = 'my_file.txt'
    kooka.display.setfont(fonts.mono6x7)
    kooka.display.print('Printing', filename, show=0)
    f = open(filename,'rt')
    line = ''
    # Loop that reads and prints each line of the file
    for line in f:
        kooka.display.print(line, show=0)
    kooka.display.print('End', show=0)

# Main loop code, run continuously.
while True:
    kooka.display.show()
    machine.idle()

# Generated Blockly XML follows
# <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="[|L|wO^Hm{K5mx7WaG?a">filename</variable><variable id="w?cjql=hCM4q!Z-e3i7j">f</variable><variable id="kROrjx$YZ$Q+?HH^P!?2">line</variable></variables><block type="event_on_start" id="m3@r/?40keqRH0s3p,n[" x="50" y="-390"><statement name="DO"><block type="py_stmt" id="kL+6$kuFV0]jm~]pwu,Y"><field name="STMT"># Open the text file for reading</field><next><block type="variables_set" id="$RR:dC!!*IsMUTEoT0sS"><field name="VAR" id="[|L|wO^Hm{K5mx7WaG?a">filename</field><value name="VALUE"><block type="text" id="I,kPS_eHY0^NRoGQ4@hN"><field name="TEXT">my_file.txt</field></block></value><next><block type="display_setfont" id="1Q+`WBTHKi6kZ.Q7oE,f"><field name="FONT">mono6x7</field><next><block type="display_print2" id="_0+m8L~@Ufe,]G!jH^Bz"><value name="VALUE1"><shadow type="text" id="/8@;Ecm/_nq;,MQ)W0Ol"><field name="TEXT">Printing</field></shadow></value><value name="VALUE2"><shadow type="math_number" id="qUL+N+AI:PG;b3qheXNq"><field name="NUM">123</field></shadow><block type="variables_get" id="-fm-MK0;da(mg]0|itdd"><field name="VAR" id="[|L|wO^Hm{K5mx7WaG?a">filename</field></block></value><next><block type="variables_set" id="jc:7y)F(:~0d^08v|AYh"><field name="VAR" id="w?cjql=hCM4q!Z-e3i7j">f</field><value name="VALUE"><block type="py_expr" id="A}D,?M.2GMu1#|)T5?Sw"><field name="EXPR">open(filename,'rt')</field></block></value><next><block type="variables_set" id="J[{HI_EQPJKq`A{K6OP7"><field name="VAR" id="kROrjx$YZ$Q+?HH^P!?2">line</field><value name="VALUE"><block type="text" id="~6%eeuZXf4k$KeM+dZ7~"><field name="TEXT"></field></block></value><next><block type="py_stmt" id="=Jp).ngX~Cb097m106l~"><field name="STMT"># Loop that reads and prints each line of the file</field><next><block type="controls_forEach" id="*!D5aTRn,H**^XQZJT}O"><field name="VAR" id="kROrjx$YZ$Q+?HH^P!?2">line</field><value name="LIST"><block type="variables_get" id="`XTAXR6;k0RI/z50b6MN"><field name="VAR" id="w?cjql=hCM4q!Z-e3i7j">f</field></block></value><statement name="DO"><block type="display_print" id="k3y`(709Wz1`Gbu~4,u?"><value name="VALUE"><shadow type="text" id=".EKu}twh0;-5#|``j]a)"><field name="TEXT">Hello</field></shadow><block type="variables_get" id="j^1}1.dh[=,;q}6M(ecZ"><field name="VAR" id="kROrjx$YZ$Q+?HH^P!?2">line</field></block></value></block></statement><next><block type="display_print" id="[TC532|,$=,cMQ(;6Z@B"><value name="VALUE"><shadow type="text" id="LIv3LcQem^HzZERD/Th#"><field name="TEXT">End</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block></xml>
