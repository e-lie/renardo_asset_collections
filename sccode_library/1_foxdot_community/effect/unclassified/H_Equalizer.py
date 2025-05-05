sccode = """
SynthDef.new(\\H_Equalizer, {
	|bus, high, highfreq|
	var osc;
	osc = In.ar(bus, 2);
	osc = BHiShelf.ar(osc, freq: highfreq, db: abs(high).ampdb);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="high",
    fullname="H_Equalizer",
    description="H_equalizer effect",
    code=sccode,
    arguments={
        "high": 1,
        "highfreq": 8000
    },
    order=2,
)
