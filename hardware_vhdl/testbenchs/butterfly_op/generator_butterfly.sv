
`define SV_RAND_CHECK(r) \
    do begin \
        if(!(r)) begin \
            $display("%s:%0d: Randomization failed \"%s\"", \
                     `__FILE__, `__LINE__, `"r`"); \
            &finish; \
        end \
    end while (0)

class generator;

    mailbox#(Transaction) gen2drv;
    mailbox#(Transaction) gen2mdl;
    Transaction blueprint;
    
    function new(input mailbox#(Transaction) gen2drv, input mailbox#(Transaction) gen2mdl);
        this.gen2drv = gen2drv;
        this.gen2drv = gen2mdl;
        this.blueprint = new();
    endfunction

    virtual task run(input int trials = 10);
        repeat(trials) begin
            `SV_RAND_CHECK(blueprint.randomize());
            gen2drv.put(blueprint.copy());
            gen2mdl.put(blueprint.copy());
        end
    endtask

endclass
