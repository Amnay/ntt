library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity butterfly_op is
    generic(
        DW  : in unsigned(7 downto 0) := 32
        MW  : in unsigned(7 downto 0) := 64
    );
    port(
        clk             : in  std_logic;    -- Unused
        modulo          : in  std_logic_vector(MW-1 downto 0);
        ileft, irght    : in  std_logic_vector(DW-1 downto 0);
        oleft, orght    : out std_logic_vector(DW-1 downto 0);
    );
end butterfly_op;

architecture rtl of butterfly_op is

signal a,b,c,d,e : std_logic_vector(DW downto 0);

begin
    a <= '0' & ileft;
    b <= '0' & irght;
    c <= '0' & modulo;

    d <= std_logic_vector( ( unsigned(a) + unsigned(b) ) mod unsigned(c) );
    e <= std_logic_vector( ( signed(a)   - signed(b)   ) mod signed(c)   );

    oleft <= d(DW-1 downto 0);
    orght <= e(DW-1 downto 0);

end rtl;

