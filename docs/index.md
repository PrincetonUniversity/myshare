# What is myshare?

`myshare` is a free and open-source tool that wraps Slurm `sshare` to explain queue times in plain language. It was released in 2026 under the GNU GPL v2 license. Visit the [myshare GitHub repository](https://github.com/PrincetonUniversity/myshare).

Below is sample output:

```
$ myshare
────────────────────────────────────────────────────────────────────────────────
                          Why Aren't My Jobs Running?                           
────────────────────────────────────────────────────────────────────────────────
root
└── total
    └── cses (LevelFS: 0, LevelFS Rank: 43/43)
        └── jdh4 (LevelFS: 0.06, LevelFS Rank: 82/83)

                               Fairshare: 0.0796

Bad news! Your fairshare rank is 4903 of 5327 users which puts you in the bottom
8th percentile. You should expect long queue times.

The table below shows the accounts sorted by LevelFS which is normalized
Shares divided by normalized Usage:

        Account        Shares             Usage             LevelFS         Fairshare      ActiveUsers
     ─────────────────────────────────────────────────────────────────────────────────────────────────
 1      andlinger      1  (0.0%)             0  (0.0%)   infinity       [0.9996, 0.9996]             0
 2            ias      1  (0.0%)             0  (0.0%)   infinity       [0.9996, 0.9996]             0
 3            nes      1  (0.0%)             0  (0.0%)   infinity       [0.9996, 0.9996]             0
 4           pcts      1  (0.0%)             0  (0.0%)   infinity       [0.9996, 0.9996]             0
 5        complit      1  (0.0%)             0  (0.0%)   2.81e+12       [0.9968, 0.9976]             0
 6   architecture      1  (0.0%)        352482  (0.0%)         37       [0.9959, 0.9966]             4
 7        history      1  (0.0%)        906426  (0.0%)         14       [0.9878, 0.9957]             3
 8            eas      1  (0.0%)        984532  (0.0%)         13       [0.9876, 0.9876]             1
 9            shs   2112 (21.4%)    2965678848  (2.3%)          9       [0.9827, 0.9874]            24
10       subotnik   1728 (17.5%)    2452948311  (1.9%)          9       [0.9788, 0.9825]            15
11        jenkins    768  (7.8%)    5851521671  (4.6%)          1.7     [0.9660, 0.9786]            36
12            pni    576  (5.8%)    6955590404  (5.4%)          1.1     [0.8881, 0.9658]           154
13           math      1  (0.0%)      14003795  (0.0%)          0.9     [0.8870, 0.8879]             3
14       politics     14  (0.1%)     201902624  (0.2%)          0.9     [0.8677, 0.8868]            28
15            cbe   1344 (13.6%)   20013357641 (15.7%)          0.9     [0.8234, 0.8675]           103
16        physics   1024 (10.4%)   15901187763 (12.4%)          0.8     [0.7509, 0.8232]           116
17           orfe    160  (1.6%)    2747967621  (2.2%)          0.8     [0.7319, 0.7507]            46
18     psychology    192  (1.9%)    3345713891  (2.6%)          0.7     [0.7100, 0.7317]            50
19           chem    960  (9.7%)   20015127039 (15.7%)          0.6     [0.6471, 0.7098]           128
20             ee    253  (2.6%)    7907078108  (6.2%)          0.4     [0.5545, 0.6469]           232
21           ddss      1  (0.0%)      33204746  (0.0%)          0.4     [0.5532, 0.5543]             4
22            rse      1  (0.0%)      36455567  (0.0%)          0.4     [0.5440, 0.5530]            11
23       genomics    576  (5.8%)   21840053313 (17.1%)          0.3     [0.4963, 0.5438]           109
24            cdh      1  (0.0%)      43991966  (0.0%)          0.3     [0.4946, 0.4962]             2
25       classics      1  (0.0%)      45061863  (0.0%)          0.3     [0.4933, 0.4945]             4
26           spia     15  (0.2%)     726251352  (0.6%)          0.3     [0.4689, 0.4931]            53
27            eeb     50  (0.5%)    2869022959  (2.2%)          0.2     [0.4308, 0.4687]            59
28          music      1  (0.0%)      59871052  (0.0%)          0.2     [0.4288, 0.4306]             3
29            geo      6  (0.1%)     493387636  (0.4%)          0.2     [0.4062, 0.4286]            35
30            cee     16  (0.2%)    1405402362  (1.1%)          0.1     [0.3726, 0.4060]            71
31         molbio     20  (0.2%)    1761020832  (1.4%)          0.1     [0.3156, 0.3724]           100
32     philosophy      1  (0.0%)      96000226  (0.1%)          0.1     [0.3131, 0.3154]             7
33          astro     11  (0.1%)    1327738144  (1.0%)          0.1     [0.2859, 0.3129]            56
34     humanities      1  (0.0%)     133259646  (0.1%)          0.1     [0.2848, 0.2857]             4
35            aos      1  (0.0%)     155402815  (0.1%)          0.08    [0.2812, 0.2846]             6
36         bioeng      1  (0.0%)     282855685  (0.2%)          0.05    [0.2805, 0.2810]             4
37          socio      1  (0.0%)     518488255  (0.4%)          0.03    [0.2666, 0.2803]            35
38           pacm      1  (0.0%)     520719363  (0.4%)          0.02    [0.2630, 0.2664]            15
39            mae      4  (0.0%)    2102082439  (1.6%)          0.02    [0.2185, 0.2628]            83
40           pppl      1  (0.0%)     755232046  (0.6%)          0.02    [0.2101, 0.2183]             8
41           econ      1  (0.0%)     790028078  (0.6%)          0.02    [0.1939, 0.2099]            23
42             cs      1  (0.0%)    3384038662  (2.6%)          0.004   [0.0950, 0.1937]           224
43           cses      0  (0.0%)       1757393  (0.0%)          0       [0.0794, 0.0948]            15

  In the table above, the minimum and maximum Fairshare values of the users within
  each account are shown. Fairshare values are assigned in segments. The users
  within the account with the highest LevelFS are assigned the highest Fairshare
  values. The higher your Fairshare, the shorter your queue time.

────────────────────────────────────────────────────────────────────────────────
For more details about your cluster share, run the following command:
    $ stree -v | less
```
