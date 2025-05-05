sccode = """
SynthDef.new(\\FrequencyModulationSaw,
{|bus, fm_saw, fm_saw_i|
var osc;
osc = In.kr(bus, 1);
osc = osc + (fm_saw_i * Saw.kr(osc * fm_saw));
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="fm_saw",
    fullname="FrequencyModulationSaw",
    description="Frequencymodulationsaw effect",
    code=sccode,
    arguments={
        "fm_saw": 0,
        "fm_saw_i": 1
    },
    order=0,
)
