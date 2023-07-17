from datetime import datetime
def create_newname():
    dn=datetime.now()
    newname=dn.strftime('%Y%m%d%H%M')
    return('A'+newname)
