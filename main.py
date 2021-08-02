# Anh Do (Student ID #001511153)
import readPackage
from readPackage import get_package_hash_table

print('WGUPS Routing Program')
package = int(input('Status for package: '))

packageHashTable = get_package_hash_table()
print(packageHashTable.get(package))


