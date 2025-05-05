sccode = """
SynthDef.new(\\feeddelay, {
	|bus, feed, feedfreq|
	var osc,out;
	osc = In.ar(bus, 2);
	out = osc + Fb({		arg feedback;		osc = CombN.ar(HPF.ar(feedback*feed, feedfreq) + osc, 0.5, 0.25).tanh;	},0.5,0.125);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="feed",
    fullname="feeddelay",
    description="Feeddelay effect",
    code=sccode,
    arguments={
        "feed": 0.7,
        "feedfreq": 50
    },
    order=2,
)
