#! ['module foo']
import pkg1.foo
#! ['bar=1']
pkg1.foo.bar

#! ['module sub']
import pkg1.sub
#! ['module bar']
import pkg1.sub.bar
#! ['foo=2']
pkg1.sub.bar.foo
