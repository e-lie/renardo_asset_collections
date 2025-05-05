sccode = """
SynthDef.new(\\DFM1,
{|bus, dfm, dfmr, dfmd|
var osc;
osc = In.ar(bus, 2);
osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="dfm",
    fullname="DFM1",
    description="Dfm1 effect",
    code=sccode,
    arguments={
        "dfm": 0,
        "dfmr": 0.1,
        "dfmd": 1
    },
    order=2,
)
