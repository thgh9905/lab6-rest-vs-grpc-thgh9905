
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|
|   REST add	|   2.3770147860004727	|   2.3913779610002166	|  320.3788785600045	|
|   gRPC add	|   0.8096818430003623	|   0.9151106849999451	|   147.6756372300042 	|
|   REST rawimg	|   4.414566145999743	|   40.388733254000726	|   1342.4620546999904	|
|   gRPC rawimg	|   13.156322886999988    |   20.46726627099997	|   613.957369399941	|
|   REST dotproduct	|   2.8560065120000218	|   3.0971102849998715	|  338.508504499996	|
|   gRPC dotproduct	|   0.8607469199996558	|   0.9270489569998972	|   145.17793643000005	|
|   REST jsonimg	|   207.63796563600044	|   55.34894294999958	|   1459.2005591000088	|
|   gRPC jsonimg	|   109.13095248699938    |   57.20831339100005	|   325.0868332999744	|
|   PING        |   0.041    |   0.282   |   160.131    |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

Using the SSH terminal of the Frankfurt VM in Europe already feels like it has more latency as I type into that terminal. It isn't surprising that pinging localhost has the lowest latency and the Frankfurt VM in Europe has the highest latency, in which the round trip time between the VM in the Western US and the VM in Europe is much higher than the round trip times of the other categories. With that increased latency in the Europe server, there would be the highest execution times per operation for every operation, except for the jsonimage operation for the REST localhost server. If REST makes a new TCP connection for every query, that means there would have to be a TCP handshake for every query, which takes more time, while gRPC saves time by not needing to take the time to do a handshake for every query.