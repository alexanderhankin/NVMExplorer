#initialize class for cryomem output class, to be extracted from parsed cryomem results and pickled as input to the analytical model
#per-technology specifications can be inherit
from nvmexplorer_src.input_defs.cell_cfgs import *

class CryoMEMInputConfig:
  def __init__(self,
                mem_cfg_file_path="../../data/mem_cfgs/test_SRAM.cfg", #path to cryomem cfg input
		process_node=45, #chosen node in nm
		opt_target="ReadLatency", #optimization target
		word_width=64, #word width in bits
		capacity=4, #capacity in MB
		cell_type=SRAMCellConfig(), #pass the cell configuration
        stacked_die_count=1,
        partition_granularity=0,
        local_tsv_projection=0,
        global_tsv_projection=0,
        tsv_redundancy=1.0,
        monolithic_layer_count=1,
        allow_difference_tag_tech=1,
        memory_cell_input_file="",
        print_all_optimals=0,
        force_bank_3d="",
        force_bank_3da="",
        force_bank_a="",
        print_level=0

		):
    self.mem_cfg_file_path = mem_cfg_file_path
    self.process_node = process_node
    self.opt_target = opt_target
    self.word_width = word_width
    self.capacity = capacity
    self.cell_type = cell_type
    self.stacked_die_count = stacked_die_count
    self.partition_granularity = partition_granularity
    self.local_tsv_projection = local_tsv_projection
    self.global_tsv_projection = global_tsv_projection
    self.tsv_redundancy = tsv_redundancy
    self.monolithic_layer_count = monolithic_layer_count
    self.allow_difference_tag_tech = allow_difference_tag_tech
    self.memory_cell_input_file = memory_cell_input_file
    self.print_all_optimals = print_all_optimals
    self.force_bank_3d = force_bank_3d
    self.force_bank_3da = force_bank_3da
    self.force_bank_a = force_bank_a
    self.print_level = print_level


  def generate_mem_cfg(self):
    """ Creates a memory config file using characteristics of :class:`CryoMEMInputConfig` object 
    to be used as an input to CryoMEM
    """
    cfg_file = open(self.mem_cfg_file_path, "w+")
    cfg_file.write(self.cell_type.mem_cfg_base)
    cfg_file.write("-ProcessNode: %d\n" % self.process_node+"\n")
    cfg_file.write("-OptimizationTarget: "+self.opt_target+"\n")
    cfg_file.write("-WordWidth (bit): %d\n" % self.word_width+"\n")
    cfg_file.write("-Capacity (MB): %d\n" % self.capacity+"\n") 
    cfg_file.write("-StackedDieCount: %d\n" % self.stacked_die_count+"\n") #- Number of dies over which the memory is distributed
    cfg_file.write("-PartitionGranularity: %d\n" % self.partition_granularity+"\n")  
    #0: Coarse granularity: This assumes that address, control, and data signals are 
    #broadcast to all stacked dies and decoded on the destination die. 
    #1: Fine granularity: This assumes that address signals are pre-decoded on a 
    #separate logic layer and the undecoded address signals are broadcast to all 
    #stacked dies. The control and data are still shared. 
    #Note that the total number of dies in fine granularity is StackedDieCount + 1
    cfg_file.write("-LocalTSVProjection: %d\n" % self.local_tsv_projection+"\n")  
    #0: Use aggressive TSV projection from ITRS for local TSVs.
    #1: Use conservative values from industry measurements for local TSVs
    #Local TSVs are used in fine granularity partitioning to route pre-decoded signals
    cfg_file.write("-GlobalTSVProjection: %d\n" % self.global_tsv_projection+"\n") 
    #0: Use aggressive TSV projection from ITRS for global TSVs
    #1: Use conservative values from industry measurements for global TSVs
    #Global TSVs are used in both fine and coarse granularity partitioning to 
    #route broadcast signals (e.g., data and control signals)
    cfg_file.write("-TSVRedundancy: %f\n" % self.tsv_redundancy+"\n") #Any floating point value from 1.0 or higher (reasonably, about 
    #2.0 is the maximum). ((TSVRedundancy - 1)*100) is the percentage of extra TSVs 
    #assumed for each TSV cluster for fault tolerance / TSV yield issues.
    cfg_file.write("-MonolithicStackCount: %d\n" % self.monolithic_layer_count+"\n") #Integer value e.g., 1, 2, 4. This is the number of memory 
    #layers on the *same* die which are monolithically stacked.
    #cfg_file.write("-AllowDifferenceTagTech: %d\n" % self.allow_difference_tag_tech+"\n") #Allow the tag array of a cache to be a different 
    #technology than the data array (e.g., SRAM tag array with STT-RAM data array).
    #cfg_file.write("-MemoryCellInputFile: ".format(self.memory_cell_input_file)+"\n") #This parameter can be specified multiple times 
    #to consider multiple different technologies in the same simulation run.
    #cfg_file.write("-PrintAllOptimals: %d\n" % self.print_all_optimals+"\n") #Print the optimal design for each optimization 
    #target (can be used to find the best of multiple technology inputs).
    #cfg_file.write("-ForceBank3D: ".format(self.force_bank_3d)+"\n") #Dimensions of each bank in terms of number of Mats in each direction.
    #cfg_file.write("-ForceBank3DA: ".format(self.force_bank_3da)+"\n") #Same as ForceBank3D, except forcing the number of active Mats is not required
    #cfg_file.write("-ForceBankA: ".format(self.force_bank_a)+"\n") #Same as ForceBank in NVSim, except forcing the number of active Mats is not required.
    cfg_file.write("-PrintLevel: %d\n" % self.print_level+"\n") #0 -> does NOT produce CACHE DATA ARRAY DETAILS and CACHE TAG ARRAY DETAILS
    #1 -> produces CACHE DATA ARRAY DETAILS and CACHE TAG ARRAY DETAILS 
    if self.cell_type.mlc > 1:
      cell_levels = 2**(self.cell_type.mlc)
      cfg_file.write("-CellLevels: %d\n" % cell_levels+"\n")
    cfg_file.close()

class CryoMEMOutputConfig: #initialized to 16nm SRAM, 4MB
  def __init__(self,
		exp_name="default", #name or ID
		#retain relevant CryoMEM configs
		input_cfg = CryoMEMInputConfig(),
		#also define all relevant outputs
		read_latency=-1, #ns
		read_bw=-1, #GB/s
		read_energy=-1, #pJ/access
		write_latency=-1, #ns
		write_bw=-1, #GB/s
		write_energy=-1, #nJ/access
		leakage_power=-1, #mW
		area=-1, #mm^2
		area_efficiency=-1 #percentage
		):
    # define all parameters
    self.exp_name = exp_name
    self.input_cfg = input_cfg
    self.read_latency = read_latency
    self.read_bw = read_bw
    self.read_energy = read_energy
    self.write_latency = write_latency
    self.write_bw = write_bw
    self.write_energy = write_energy
    self.leakage_power = leakage_power
    self.area = area
    self.area_efficiency = area_efficiency

  def print_summary(self):
    """ Prints a summary of the parsed CryoMEM output results
    """
    print("Experiment Name: "+self.exp_name)
    print("Read Latency (ns): %f" % self.read_latency)
    print("Read BW (GB/s): %f" % self.read_bw)
    print("Write Latency (ns): %f" % self.write_latency)
    print("Write BW (GB/s): %f" % self.write_bw)
    print("Read Energy (pJ): %f" % self.read_energy)
    print("Write Energy (pJ): %f" % self.write_energy)
    print("Leakage Power (mW): %f" % self.leakage_power)
    print("Area (mm^2): %f" % self.area)
    print("Area Efficiency (percent): %f" % self.area_efficiency)

def parse_cryomem_output(filepath='output_examples/sram_0', input_cfg=CryoMEMInputConfig()):
  """ Returns a :class:`CryoMEMOutputConfig` object which gets populated with the output results in
  parsed from file_path. 

  :param filepath: path to CryoMEM output file
  :type filepath: String
  :param input_cfg: :class:`CryoMEMIntputConfig` object that was used to create the CryoMEM output 
  :type input_cfg: :class:`CryoMEMInputConfig` object
  :return: :class:`CryoMEMOutputConfig` object containing parsed CryoMEM results
  :rtype: :class:`CryoMEMOutputConfig`
  """
  #initialize base
  base = CryoMEMOutputConfig(input_cfg=input_cfg)

  num_banks = 0
  block_size = 0

  with open(filepath, 'r') as f:
    print("File path in parse_cryomem_output")
    print(filepath)
    lines = f.readlines()

  
  # Get rid of new lines
  lines = map(lambda x: x.rstrip(), lines)
  print("here")

  for line in lines:
    if 'Data array: Area (mm2)' in line and (base.area == -1):
      base.area = float(line.split(": ")[2])
    elif 'Access time (ns):' in line and (base.read_latency == -1):
      base.read_latency = float(line.split(":")[1])
      base.write_latency = float(line.split(":")[1])
    elif 'Number of banks:' in line:
      num_banks = float(line.split(":")[1])
    elif 'Area efficiency (Memory cell area/Total area) -' in line:
      base.area_efficiency = float((line.split("-")[1]).replace('%', ''))
    elif 'Block size (bytes):' in line:
      block_size = float(line.split(":")[1])
    elif 'Total dynamic read energy per access (nJ):' in line:
      base.read_energy = float(line.split(":")[1])
      base.read_energy = base.read_energy * 1000.
    elif 'Total leakage power of a bank (mW):' in line:
      base.leakage_power = float(line.split(":")[1])*num_banks
    elif 'Total dynamic write energy per access (nJ):' in line:
      base.write_energy = float(line.split(":")[1])
      base.write_energy = base.write_energy * 1000.
      
    base.read_bw = block_size/base.read_latency
    base.write_bw = block_size/base.write_latency
        
  return base

if __name__ == '__main__':
  #test mem cfg definition and output parsing
  test_input_cfg = CryoMEMInputConfig()
  test_input_cfg.cell_type.generate_cell_file()
  test_input_cfg.cell_type.append_cell_file()
  
  test_input_cfg.generate_mem_cfg()

  print("Memory config generation test complete.")


