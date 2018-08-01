
testValues = [
    {
        'enemyFirePower' : 86,
        'enemyMobility'  : 170,
        'ourMobility'    : 55
    },
    {
        'enemyFirePower' : 100,
        'enemyMobility'  : 1,
        'ourMobility'    : 170
    },
    {
        'enemyFirePower' : 100,
        'enemyMobility'  : 170,
        'ourMobility'    : 10
    },
    {
        'enemyFirePower' : 100,
        'enemyMobility'  : 40,
        'ourMobility'    : 170
    }
]


for values in testValues:
    enemyFirePower = values['enemyFirePower']
    enemyMobility = values['enemyMobility']
    ourMobility = values['ourMobility']

    damageStolen = enemyFirePower * min( (ourMobility/enemyMobility) * 0.3 , 1 )

    percent = (damageStolen / enemyFirePower) * 100

    print('damageStolen: ', damageStolen, ';', percent, 'percent of', enemyFirePower, 'damage')
