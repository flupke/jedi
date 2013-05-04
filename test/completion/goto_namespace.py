#! ['module sub']
import pkg1.sub
#! ['module bar']
import pkg1.sub.bar
#! ['foo=2']
pkg1.sub.bar.foo


#! ['module sub2']
import pkg1.sub2
#! ['module foo']
import pkg1.sub2.foo
#! ['bar=1']
pkg1.sub2.foo.bar
