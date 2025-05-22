sccode = """
SynthDef.new(\\M_Equalizer, {
	|bus, mid, midfreq, midq|
	var osc;
	osc = In.ar(bus, 2);
	osc = BPeakEQ.ar(osc, freq: midfreq, rq: midq.reciprocal, db: abs(mid).ampdb);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="mid",
    fullname="M_Equalizer",
    description="M_equalizer effect",
    code=sccode,
    arguments={
        "mid": 1,
        "midfreq": 1000,
        "midq": 1
    },
    order=2,
)
