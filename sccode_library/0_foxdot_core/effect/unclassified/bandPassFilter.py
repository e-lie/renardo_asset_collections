sccode = """
SynthDef.new(\\bandPassFilter,
{|bus, bpf, bpr, bpnoise, sus|
var osc;
osc = In.ar(bus, 2);
bpnoise = bpnoise / sus;
bpf = LFNoise1.kr(bpnoise).exprange(bpf * 0.5, bpf * 2);
bpr = LFNoise1.kr(bpnoise).exprange(bpr * 0.5, bpr * 2);
osc = BPF.ar(osc, bpf, bpr);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="bpf",
    fullname="bandPassFilter",
    description="Bandpassfilter effect",
    code=sccode,
    arguments={
        "bpf": 0,
        "bpr": 1,
        "bpnoise": 0,
        "sus": 1
    },
    order=2,
)
