
class Driver;

    mailbox#(Transaction) gen2drv;
    
    function new(input mailbox#(Transaction) gen2drv);
        this.gen2drv = gen2drv;
    endfunction
    
    virtual task run();
        Transaction tr;
        
        forever begin
            gen2drv.get(tr);
            @ifc.cb;
            ifc.cb.left     <= tr.ileft;
            ifc.cb.rght     <= tr.irght;
            ifc.cb.modulo   <= tr.modulo;
        end
    endtask

endclass
