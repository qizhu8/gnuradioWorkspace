Today, I tried the following two things
1. use the gnuradio-companion to build the graph
2. build the first OOT module

There are several key points to remember
1. when you place a block, pay great attention to he io type. Sometime, the default type is float, but the out-to-be type is complex, there is a comflict
2. if you want to make your block general, use the parameter block or variable block. parameter block can store string, and is more flexible

3. when built my own module, I use the default command $ gr_modtool newmod gr_square_ff
when build the test_case in ./python/, the generated function name is not "test_001_square_ff", it was "test_001_t". You should pay greate attention to this. Besides, I mistype 'blocks' to 'block', this is another type.
4. when changing the cpp file, pay attention to the "<+xxx+>", do not forget to delete "<"

that's it