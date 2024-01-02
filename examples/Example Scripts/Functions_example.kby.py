import machine, kooka
import time

# Works out the Kookaberry's orientation.
def direction():
    if kooka.accel.get_xyz()[2] < 0:
        return 'up'
    return 'down'



# Initialise timer counters.
_timer1000 = time.ticks_ms()

# Main loop code, run continuously.
while True:
    if time.ticks_diff(time.ticks_ms(), _timer1000) >= 0:
        _timer1000 += 1000
        kooka.display.clear()
        kooka.display.print(direction(), show=0)
        kooka.display.show()
    kooka.display.show()
    machine.idle()

# Generated Blockly XML follows
# <xml xmlns="https://developers.google.com/blockly/xml"><block type="event_every_seconds" id="APw$l`F71sD9Z;fD{J(S" x="210" y="-170"><field name="T">1</field><statement name="DO"><block type="display_clear" id="QTA?lA6kd=9kt1O#h{t8"><next><block type="display_print" id="flI9g+#q,P+j(#M)#Gr0"><value name="VALUE"><shadow type="text" id="Xcpvuu{,yuhjUG6Bi~:s"><field name="TEXT">Hello</field></shadow><block type="procedures_callreturn" id="8@s*`{u,RK:mF^(dKZ+D"><mutation name="direction"></mutation></block></value><next><block type="display_show" id="^WFWb%LkBAG5iBbZx0op"></block></next></block></next></block></statement></block><block type="procedures_defreturn" id="ttJv8A.n?hmFv7sTPnd?" x="210" y="-30"><field name="NAME">direction</field><comment pinned="false" h="80" w="160">Works out the Kookaberry's orientation.</comment><statement name="STACK"><block type="procedures_ifreturn" id="6hIrNF[FM+.ER?Oal%Y;"><mutation value="1"></mutation><value name="CONDITION"><block type="logic_compare" id="be9iC_GHlQ%UX)_F;N3/"><field name="OP">LT</field><value name="A"><block type="internal_accel_axis" id="T:IC/_o%+$?uX)FS}p*L"><field name="AXIS">2</field></block></value><value name="B"><block type="math_number" id="_%}L!j#)-yLJFys}JRMX"><field name="NUM">0</field></block></value></block></value><value name="VALUE"><block type="text" id="~7?%{6PMk;g3f$^F6=w3"><field name="TEXT">up</field></block></value></block></statement><value name="RETURN"><block type="text" id="^1U?xmgJ`xJN(-z`-mU{"><field name="TEXT">down</field></block></value></block></xml>
