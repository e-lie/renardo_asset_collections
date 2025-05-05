sccode = """
SynthDef.new(\\FrequencyModulationSine,
{|bus, fm_sin, fm_sin_i|
var osc;
osc = In.kr(bus, 1);
osc = osc + (fm_sin_i * SinOsc.kr(osc * fm_sin));
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="fm_sin",
    fullname="FrequencyModulationSine",
    description="Frequencymodulationsine effect",
    code=sccode,
    arguments={
        "fm_sin": 0,
        "fm_sin_i": 1
    },
    order=0,
)
