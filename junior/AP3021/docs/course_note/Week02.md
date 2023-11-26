# Week02

值越大誤差越大

要存取較大的值，exponent 也要跟著變大，不過位元數是固定的，所以準確度會降低

chopping rounding

Note: In the interest of making this somewhat self-contained, I am using terminology from the most recent versions of the IEEE-754 standard. Prior to 2008, "subnormal numbers" were called "denormal numbers", and "binary32" was called "single precision". Some textbooks/papers/etc may use the old terms.

The representation that you are talking about here is called, in IEEE-754, normal numbers. A normal number is one which has a single nonzero digit on the left-hand side of the radix point (i.e. decimal point or binary point) of its mantissa.

The representation for zero uses a slightly different representation, namely, subnormal numbers.