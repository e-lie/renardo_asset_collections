sccode = """
SynthDef.new(\\L_Equalizer, {
	|bus, low, lowfreq|
	var osc;
	osc = In.ar(bus, 2);
	osc = BLowShelf.ar(osc, freq: lowfreq, db: abs(low).ampdb);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="low",
    fullname="L_Equalizer",
    description="L_equalizer effect",
    code=sccode,
    arguments={
        "low": 1,
        "lowfreq": 80
    },
    order=2,
)
