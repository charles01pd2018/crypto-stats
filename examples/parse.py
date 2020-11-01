# Examples of parsing through data sets
 
    # print( data.groupby( 'TIME' )[ 'PRICE' ].value_counts( normalize=True ) )
    
    # print( data.groupby( 'PRICE' )[ 'TIME' ].mean() )

    # print( data.corr() )

    # data[ 'high_price' ] = data.PRICE.apply(lambda x: x > 200 )
    # print ( data.corr() )

    # print( data.describe( percentiles=[ .05, .1, .5, .9, .95 ] ) )

    # cross_tab = pd.crosstab( data[ 'PRICE' ], data.TIME, normalize=True )
    # print(cross_tab)