
class Environment

    Generator gen;
    Driver drv;
    Model mdl;
    Monitor mon;
    Checker ckr;
    mailbox#(Transaction) gen2drv, gen2mdl, mdl2ckr, mon2ckr;
    
    virtual function void build();
        this.gen2drv = new();
        this.gen = new(gen2drv, gen2mdl);
        this.drv = new(gen2drv);
        this.mdl = new(gen2mdl, mdl2ckr);
        this.mon = new(mon2ckr);
        this.ckr = new(mdl2ckr, mon2ckr);
    endfunction

    virtual task run();
        fork
            gen.run();
            drv.run();
            mdl.run();
            mon.run();
            ckr.run();
        join
    endtask
    
endclass
