sccode = """
SynthDef.new(\\comp,
{|bus, comp, comp_down, comp_up|
var osc;
osc = In.ar(bus, 2);
osc = Compander.ar(osc, osc, thresh: comp, slopeAbove: comp_down, slopeBelow: comp_up, clampTime: 0.01, relaxTime: 0.01, mul: 1);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="comp",
    fullname="comp",
    description="Comp effect",
    code=sccode,
    arguments={
        "comp": 0,
        "comp_down": 1,
        "comp_up": 0.8
    },
    order=2,
)
