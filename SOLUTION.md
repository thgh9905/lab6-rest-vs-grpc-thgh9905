
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|
|   REST add	|   	|   2.3913779610002166	|  	|
|   gRPC add	|   	|   0.9151106849999451	|    	|
|   REST rawimg	|   	|   40.388733254000726	|   	|
|   gRPC rawimg	|       |   20.46726627099997	|   	|
|   REST dotproduct	|   	|   	|  	|
|   gRPC dotproduct	|   	|   0.9270489569998972	|    	|
|   REST jsonimg	|   	|   	|   	|
|   gRPC jsonimg	|       |   57.20831339100005	|   	|
|   PING        |       |   0.282   |       |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.