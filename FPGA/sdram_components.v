// sdram_components.v

// Generated using ACDS version 16.1 196

`timescale 1 ps / 1 ps
module sdram_components (
		input  wire        clk_50_clk,                          //                clk_50.clk
		input  wire        read_master_control_fixed_location,  //   read_master_control.fixed_location
		input  wire [31:0] read_master_control_read_base,       //                      .read_base
		input  wire [31:0] read_master_control_read_length,     //                      .read_length
		input  wire        read_master_control_go,              //                      .go
		output wire        read_master_control_done,            //                      .done
		output wire        read_master_control_early_done,      //                      .early_done
		input  wire        read_master_user_read_buffer,        //      read_master_user.read_buffer
		output wire [31:0] read_master_user_buffer_output_data, //                      .buffer_output_data
		output wire        read_master_user_data_available,     //                      .data_available
		input  wire        reset_reset_n,                       //                 reset.reset_n
		output wire [12:0] sdram_controller_wire_addr,          // sdram_controller_wire.addr
		output wire [1:0]  sdram_controller_wire_ba,            //                      .ba
		output wire        sdram_controller_wire_cas_n,         //                      .cas_n
		output wire        sdram_controller_wire_cke,           //                      .cke
		output wire        sdram_controller_wire_cs_n,          //                      .cs_n
		inout  wire [31:0] sdram_controller_wire_dq,            //                      .dq
		output wire [3:0]  sdram_controller_wire_dqm,           //                      .dqm
		output wire        sdram_controller_wire_ras_n,         //                      .ras_n
		output wire        sdram_controller_wire_we_n,          //                      .we_n
		input  wire        write_master_control_fixed_location, //  write_master_control.fixed_location
		input  wire [31:0] write_master_control_write_base,     //                      .write_base
		input  wire [31:0] write_master_control_write_length,   //                      .write_length
		input  wire        write_master_control_go,             //                      .go
		output wire        write_master_control_done,           //                      .done
		input  wire        write_master_user_write_buffer,      //     write_master_user.write_buffer
		input  wire [31:0] write_master_user_buffer_input_data, //                      .buffer_input_data
		output wire        write_master_user_buffer_full        //                      .buffer_full
	);

	wire         write_master_avalon_master_waitrequest;              // mm_interconnect_0:write_master_avalon_master_waitrequest -> write_master:master_waitrequest
	wire  [31:0] write_master_avalon_master_address;                  // write_master:master_address -> mm_interconnect_0:write_master_avalon_master_address
	wire   [3:0] write_master_avalon_master_byteenable;               // write_master:master_byteenable -> mm_interconnect_0:write_master_avalon_master_byteenable
	wire         write_master_avalon_master_write;                    // write_master:master_write -> mm_interconnect_0:write_master_avalon_master_write
	wire  [31:0] write_master_avalon_master_writedata;                // write_master:master_writedata -> mm_interconnect_0:write_master_avalon_master_writedata
	wire   [1:0] write_master_avalon_master_burstcount;               // write_master:master_burstcount -> mm_interconnect_0:write_master_avalon_master_burstcount
	wire  [31:0] read_master_avalon_master_readdata;                  // mm_interconnect_0:read_master_avalon_master_readdata -> read_master:master_readdata
	wire         read_master_avalon_master_waitrequest;               // mm_interconnect_0:read_master_avalon_master_waitrequest -> read_master:master_waitrequest
	wire  [31:0] read_master_avalon_master_address;                   // read_master:master_address -> mm_interconnect_0:read_master_avalon_master_address
	wire         read_master_avalon_master_read;                      // read_master:master_read -> mm_interconnect_0:read_master_avalon_master_read
	wire   [3:0] read_master_avalon_master_byteenable;                // read_master:master_byteenable -> mm_interconnect_0:read_master_avalon_master_byteenable
	wire         read_master_avalon_master_readdatavalid;             // mm_interconnect_0:read_master_avalon_master_readdatavalid -> read_master:master_readdatavalid
	wire   [1:0] read_master_avalon_master_burstcount;                // read_master:master_burstcount -> mm_interconnect_0:read_master_avalon_master_burstcount
	wire         mm_interconnect_0_sdram_controller_s1_chipselect;    // mm_interconnect_0:sdram_controller_s1_chipselect -> sdram_controller:az_cs
	wire  [31:0] mm_interconnect_0_sdram_controller_s1_readdata;      // sdram_controller:za_data -> mm_interconnect_0:sdram_controller_s1_readdata
	wire         mm_interconnect_0_sdram_controller_s1_waitrequest;   // sdram_controller:za_waitrequest -> mm_interconnect_0:sdram_controller_s1_waitrequest
	wire  [24:0] mm_interconnect_0_sdram_controller_s1_address;       // mm_interconnect_0:sdram_controller_s1_address -> sdram_controller:az_addr
	wire         mm_interconnect_0_sdram_controller_s1_read;          // mm_interconnect_0:sdram_controller_s1_read -> sdram_controller:az_rd_n
	wire   [3:0] mm_interconnect_0_sdram_controller_s1_byteenable;    // mm_interconnect_0:sdram_controller_s1_byteenable -> sdram_controller:az_be_n
	wire         mm_interconnect_0_sdram_controller_s1_readdatavalid; // sdram_controller:za_valid -> mm_interconnect_0:sdram_controller_s1_readdatavalid
	wire         mm_interconnect_0_sdram_controller_s1_write;         // mm_interconnect_0:sdram_controller_s1_write -> sdram_controller:az_wr_n
	wire  [31:0] mm_interconnect_0_sdram_controller_s1_writedata;     // mm_interconnect_0:sdram_controller_s1_writedata -> sdram_controller:az_data
	wire         rst_controller_reset_out_reset;                      // rst_controller:reset_out -> [mm_interconnect_0:write_master_clock_reset_reset_reset_bridge_in_reset_reset, read_master:reset, sdram_controller:reset_n, write_master:reset]

	custom_master #(
		.MASTER_DIRECTION    (0),
		.DATA_WIDTH          (32),
		.ADDRESS_WIDTH       (32),
		.BURST_CAPABLE       (1),
		.MAXIMUM_BURST_COUNT (2),
		.BURST_COUNT_WIDTH   (2),
		.FIFO_DEPTH          (128),
		.FIFO_DEPTH_LOG2     (7),
		.MEMORY_BASED_FIFO   (1)
	) read_master (
		.clk                     (clk_50_clk),                              //       clock_reset.clk
		.reset                   (rst_controller_reset_out_reset),          // clock_reset_reset.reset
		.master_address          (read_master_avalon_master_address),       //     avalon_master.address
		.master_read             (read_master_avalon_master_read),          //                  .read
		.master_byteenable       (read_master_avalon_master_byteenable),    //                  .byteenable
		.master_readdata         (read_master_avalon_master_readdata),      //                  .readdata
		.master_readdatavalid    (read_master_avalon_master_readdatavalid), //                  .readdatavalid
		.master_burstcount       (read_master_avalon_master_burstcount),    //                  .burstcount
		.master_waitrequest      (read_master_avalon_master_waitrequest),   //                  .waitrequest
		.control_fixed_location  (read_master_control_fixed_location),      //           control.export
		.control_read_base       (read_master_control_read_base),           //                  .export
		.control_read_length     (read_master_control_read_length),         //                  .export
		.control_go              (read_master_control_go),                  //                  .export
		.control_done            (read_master_control_done),                //                  .export
		.control_early_done      (read_master_control_early_done),          //                  .export
		.user_read_buffer        (read_master_user_read_buffer),            //              user.export
		.user_buffer_output_data (read_master_user_buffer_output_data),     //                  .export
		.user_data_available     (read_master_user_data_available),         //                  .export
		.master_write            (),                                        //       (terminated)
		.master_writedata        (),                                        //       (terminated)
		.control_write_base      (32'b00000000000000000000000000000000),    //       (terminated)
		.control_write_length    (32'b00000000000000000000000000000000),    //       (terminated)
		.user_write_buffer       (1'b0),                                    //       (terminated)
		.user_buffer_input_data  (32'b00000000000000000000000000000000),    //       (terminated)
		.user_buffer_full        ()                                         //       (terminated)
	);

	sdram_components_sdram_controller sdram_controller (
		.clk            (clk_50_clk),                                          //   clk.clk
		.reset_n        (~rst_controller_reset_out_reset),                     // reset.reset_n
		.az_addr        (mm_interconnect_0_sdram_controller_s1_address),       //    s1.address
		.az_be_n        (~mm_interconnect_0_sdram_controller_s1_byteenable),   //      .byteenable_n
		.az_cs          (mm_interconnect_0_sdram_controller_s1_chipselect),    //      .chipselect
		.az_data        (mm_interconnect_0_sdram_controller_s1_writedata),     //      .writedata
		.az_rd_n        (~mm_interconnect_0_sdram_controller_s1_read),         //      .read_n
		.az_wr_n        (~mm_interconnect_0_sdram_controller_s1_write),        //      .write_n
		.za_data        (mm_interconnect_0_sdram_controller_s1_readdata),      //      .readdata
		.za_valid       (mm_interconnect_0_sdram_controller_s1_readdatavalid), //      .readdatavalid
		.za_waitrequest (mm_interconnect_0_sdram_controller_s1_waitrequest),   //      .waitrequest
		.zs_addr        (sdram_controller_wire_addr),                          //  wire.export
		.zs_ba          (sdram_controller_wire_ba),                            //      .export
		.zs_cas_n       (sdram_controller_wire_cas_n),                         //      .export
		.zs_cke         (sdram_controller_wire_cke),                           //      .export
		.zs_cs_n        (sdram_controller_wire_cs_n),                          //      .export
		.zs_dq          (sdram_controller_wire_dq),                            //      .export
		.zs_dqm         (sdram_controller_wire_dqm),                           //      .export
		.zs_ras_n       (sdram_controller_wire_ras_n),                         //      .export
		.zs_we_n        (sdram_controller_wire_we_n)                           //      .export
	);

	custom_master #(
		.MASTER_DIRECTION    (1),
		.DATA_WIDTH          (32),
		.ADDRESS_WIDTH       (32),
		.BURST_CAPABLE       (1),
		.MAXIMUM_BURST_COUNT (2),
		.BURST_COUNT_WIDTH   (2),
		.FIFO_DEPTH          (128),
		.FIFO_DEPTH_LOG2     (7),
		.MEMORY_BASED_FIFO   (1)
	) write_master (
		.clk                     (clk_50_clk),                             //       clock_reset.clk
		.reset                   (rst_controller_reset_out_reset),         // clock_reset_reset.reset
		.master_address          (write_master_avalon_master_address),     //     avalon_master.address
		.master_write            (write_master_avalon_master_write),       //                  .write
		.master_byteenable       (write_master_avalon_master_byteenable),  //                  .byteenable
		.master_writedata        (write_master_avalon_master_writedata),   //                  .writedata
		.master_burstcount       (write_master_avalon_master_burstcount),  //                  .burstcount
		.master_waitrequest      (write_master_avalon_master_waitrequest), //                  .waitrequest
		.control_fixed_location  (write_master_control_fixed_location),    //           control.export
		.control_write_base      (write_master_control_write_base),        //                  .export
		.control_write_length    (write_master_control_write_length),      //                  .export
		.control_go              (write_master_control_go),                //                  .export
		.control_done            (write_master_control_done),              //                  .export
		.user_write_buffer       (write_master_user_write_buffer),         //              user.export
		.user_buffer_input_data  (write_master_user_buffer_input_data),    //                  .export
		.user_buffer_full        (write_master_user_buffer_full),          //                  .export
		.master_read             (),                                       //       (terminated)
		.master_readdata         (32'b00000000000000000000000000000000),   //       (terminated)
		.master_readdatavalid    (1'b0),                                   //       (terminated)
		.control_read_base       (32'b00000000000000000000000000000000),   //       (terminated)
		.control_read_length     (32'b00000000000000000000000000000000),   //       (terminated)
		.control_early_done      (),                                       //       (terminated)
		.user_read_buffer        (1'b0),                                   //       (terminated)
		.user_buffer_output_data (),                                       //       (terminated)
		.user_data_available     ()                                        //       (terminated)
	);

	sdram_components_mm_interconnect_0 mm_interconnect_0 (
		.clk_50_clk_clk                                             (clk_50_clk),                                          //                                           clk_50_clk.clk
		.write_master_clock_reset_reset_reset_bridge_in_reset_reset (rst_controller_reset_out_reset),                      // write_master_clock_reset_reset_reset_bridge_in_reset.reset
		.read_master_avalon_master_address                          (read_master_avalon_master_address),                   //                            read_master_avalon_master.address
		.read_master_avalon_master_waitrequest                      (read_master_avalon_master_waitrequest),               //                                                     .waitrequest
		.read_master_avalon_master_burstcount                       (read_master_avalon_master_burstcount),                //                                                     .burstcount
		.read_master_avalon_master_byteenable                       (read_master_avalon_master_byteenable),                //                                                     .byteenable
		.read_master_avalon_master_read                             (read_master_avalon_master_read),                      //                                                     .read
		.read_master_avalon_master_readdata                         (read_master_avalon_master_readdata),                  //                                                     .readdata
		.read_master_avalon_master_readdatavalid                    (read_master_avalon_master_readdatavalid),             //                                                     .readdatavalid
		.write_master_avalon_master_address                         (write_master_avalon_master_address),                  //                           write_master_avalon_master.address
		.write_master_avalon_master_waitrequest                     (write_master_avalon_master_waitrequest),              //                                                     .waitrequest
		.write_master_avalon_master_burstcount                      (write_master_avalon_master_burstcount),               //                                                     .burstcount
		.write_master_avalon_master_byteenable                      (write_master_avalon_master_byteenable),               //                                                     .byteenable
		.write_master_avalon_master_write                           (write_master_avalon_master_write),                    //                                                     .write
		.write_master_avalon_master_writedata                       (write_master_avalon_master_writedata),                //                                                     .writedata
		.sdram_controller_s1_address                                (mm_interconnect_0_sdram_controller_s1_address),       //                                  sdram_controller_s1.address
		.sdram_controller_s1_write                                  (mm_interconnect_0_sdram_controller_s1_write),         //                                                     .write
		.sdram_controller_s1_read                                   (mm_interconnect_0_sdram_controller_s1_read),          //                                                     .read
		.sdram_controller_s1_readdata                               (mm_interconnect_0_sdram_controller_s1_readdata),      //                                                     .readdata
		.sdram_controller_s1_writedata                              (mm_interconnect_0_sdram_controller_s1_writedata),     //                                                     .writedata
		.sdram_controller_s1_byteenable                             (mm_interconnect_0_sdram_controller_s1_byteenable),    //                                                     .byteenable
		.sdram_controller_s1_readdatavalid                          (mm_interconnect_0_sdram_controller_s1_readdatavalid), //                                                     .readdatavalid
		.sdram_controller_s1_waitrequest                            (mm_interconnect_0_sdram_controller_s1_waitrequest),   //                                                     .waitrequest
		.sdram_controller_s1_chipselect                             (mm_interconnect_0_sdram_controller_s1_chipselect)     //                                                     .chipselect
	);

	altera_reset_controller #(
		.NUM_RESET_INPUTS          (1),
		.OUTPUT_RESET_SYNC_EDGES   ("deassert"),
		.SYNC_DEPTH                (2),
		.RESET_REQUEST_PRESENT     (0),
		.RESET_REQ_WAIT_TIME       (1),
		.MIN_RST_ASSERTION_TIME    (3),
		.RESET_REQ_EARLY_DSRT_TIME (1),
		.USE_RESET_REQUEST_IN0     (0),
		.USE_RESET_REQUEST_IN1     (0),
		.USE_RESET_REQUEST_IN2     (0),
		.USE_RESET_REQUEST_IN3     (0),
		.USE_RESET_REQUEST_IN4     (0),
		.USE_RESET_REQUEST_IN5     (0),
		.USE_RESET_REQUEST_IN6     (0),
		.USE_RESET_REQUEST_IN7     (0),
		.USE_RESET_REQUEST_IN8     (0),
		.USE_RESET_REQUEST_IN9     (0),
		.USE_RESET_REQUEST_IN10    (0),
		.USE_RESET_REQUEST_IN11    (0),
		.USE_RESET_REQUEST_IN12    (0),
		.USE_RESET_REQUEST_IN13    (0),
		.USE_RESET_REQUEST_IN14    (0),
		.USE_RESET_REQUEST_IN15    (0),
		.ADAPT_RESET_REQUEST       (0)
	) rst_controller (
		.reset_in0      (~reset_reset_n),                 // reset_in0.reset
		.clk            (clk_50_clk),                     //       clk.clk
		.reset_out      (rst_controller_reset_out_reset), // reset_out.reset
		.reset_req      (),                               // (terminated)
		.reset_req_in0  (1'b0),                           // (terminated)
		.reset_in1      (1'b0),                           // (terminated)
		.reset_req_in1  (1'b0),                           // (terminated)
		.reset_in2      (1'b0),                           // (terminated)
		.reset_req_in2  (1'b0),                           // (terminated)
		.reset_in3      (1'b0),                           // (terminated)
		.reset_req_in3  (1'b0),                           // (terminated)
		.reset_in4      (1'b0),                           // (terminated)
		.reset_req_in4  (1'b0),                           // (terminated)
		.reset_in5      (1'b0),                           // (terminated)
		.reset_req_in5  (1'b0),                           // (terminated)
		.reset_in6      (1'b0),                           // (terminated)
		.reset_req_in6  (1'b0),                           // (terminated)
		.reset_in7      (1'b0),                           // (terminated)
		.reset_req_in7  (1'b0),                           // (terminated)
		.reset_in8      (1'b0),                           // (terminated)
		.reset_req_in8  (1'b0),                           // (terminated)
		.reset_in9      (1'b0),                           // (terminated)
		.reset_req_in9  (1'b0),                           // (terminated)
		.reset_in10     (1'b0),                           // (terminated)
		.reset_req_in10 (1'b0),                           // (terminated)
		.reset_in11     (1'b0),                           // (terminated)
		.reset_req_in11 (1'b0),                           // (terminated)
		.reset_in12     (1'b0),                           // (terminated)
		.reset_req_in12 (1'b0),                           // (terminated)
		.reset_in13     (1'b0),                           // (terminated)
		.reset_req_in13 (1'b0),                           // (terminated)
		.reset_in14     (1'b0),                           // (terminated)
		.reset_req_in14 (1'b0),                           // (terminated)
		.reset_in15     (1'b0),                           // (terminated)
		.reset_req_in15 (1'b0)                            // (terminated)
	);

endmodule
