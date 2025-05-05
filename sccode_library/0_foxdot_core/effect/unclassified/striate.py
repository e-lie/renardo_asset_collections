sccode = """
SynthDef.new(\\striate,
{|bus, striate, sus, buf, rate|
var osc;
osc = In.kr(bus, 1);
rate = (BufDur.kr(buf) / sus);
rate = Select.kr(rate > 1, [1, rate]);
osc = osc * LFPulse.ar(striate / sus, width:  (BufDur.kr(buf) / rate) / sus) * rate;
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="striate",
    fullname="striate",
    description="Striate effect",
    code=sccode,
    arguments={
        "striate": 0,
        "sus": 1,
        "buf": 0,
        "rate": 1
    },
    order=0,
)
