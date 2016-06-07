# Deprecated: Program for match-making Fire Emblem characters.
#
# Returns a list of matched characters.


########################################################################

# CREATE CHARACTER CLASS

class Character
  def initialize(name)
    @name = name
    @fiance = nil
    @preferences = []
    @proposals = []
  end
  attr_reader :name, :proposals
  attr_accessor :fiance, :preferences
 
  def to_s
    case @name
    when "femui"
      "Regina"
    else
      @name.capitalize
    end
  end
 
  def free
    @fiance = nil
  end
 
  def single?
    @fiance == nil
  end
 
  def engage(character)
    self.fiance = character
    character.fiance = self
  end
 
  def better_choice?(character)
    @preferences.index(character) < @preferences.index(@fiance)
  end
 
  def propose_to(character)
    @proposals << character
    character.respond_to(self)
  end
 
  def respond_to(character)
    if single?
      engage(character)
    elsif better_choice?(character)
      @fiance.free
      engage(character)
    else
      puts "#{self} rejects proposal from #{character}" if $DEBUG
    end
  end
end
 
 
########################################################################

# INITIALIZE THE CHARACTER'S DATA
 
prefs = {
  'xander'  => %w[abi eve cath ivy jan dee fay bea hope],
  'bob'  => %w[cath hope abi dee eve fay bea jan ivy gay],
  'col'  => %w[hope eve abi dee bea fay ivy gay cath jan],
  'dan'  => %w[ivy fay dee gay hope eve jan bea cath abi],
  'ed'   => %w[jan dee bea cath fay eve abi ivy hope gay],
  'fred' => %w[bea abi dee gay eve ivy cath jan hope fay],
  'gav'  => %w[gay eve ivy bea cath abi dee hope jan fay],
  'hal'  => %w[abi eve hope fay ivy cath jan bea gay dee],
  'ian'  => %w[hope cath dee gay bea abi fay ivy jan eve],
  'jon'  => %w[abi fay jan gay eve bea dee cath ivy hope],
  'abi'  => %w[bob fred jon gav ian xander dan ed col hal],
  'bea'  => %w[bob xander col fred gav dan ian ed jon hal],
  'cath' => %w[fred bob ed gav hal col ian xander dan jon],
  'dee'  => %w[fred jon col xander ian hal gav dan bob ed],
  'eve'  => %w[jon hal fred dan xander gav col ed ian bob],
  'fay'  => %w[bob xander ed ian jon dan fred gav col hal],
  'gay'  => %w[jon gav hal fred bob xander col ed dan ian],
  'hope' => %w[gav jon bob xander ian dan hal ed col fred],
  'ivy'  => %w[ian col hal gav fred bob xander ed jon dan],
  'jan'  => %w[ed hal gav xander bob jon col ian fred dan],
}

# This part is where the data can be seperated based on games
 
@parent_unit = Hash[
  %w[xander bob col dan ed fred gav hal ian jon].collect do |name|
    [name, Character.new(name)]
  end
]
 
@partner_unit = Hash[
  %w[abi bea cath dee eve fay gay hope ivy jan].collect do |name|
    [name, Character.new(name)]
  end
]
 
@parent_unit.each {|name, parent| parent.preferences = @partner_unit.values_at(*prefs[name])}
@partner_unit.each {|name, partner| partner.preferences = @parent_unit.values_at(*prefs[name])}
 
 
########################################################################

# PERFORMS THE MATCH MAKING
 
def match_units(parent, partner)
  parent.each_value {|parent_unit| parent_unit.free}
  partner.each_value {|partner| partner.free}
 
  while char = parent.values.find {|parent_unit| parent_unit.single?} do
    potential_mate = char.preferences.find {|partner| not char.proposals.include?(partner)}
    char.propose_to(potential_mate)
  end
end
 
match_units @parent_unit, @partner_unit
 
@parent_unit.each_value.collect {|parent| puts "#{parent} + #{parent.fiance}"}

########################################################################

# END THE PROGRAM
puts " "
puts "Press any key to end program."
endProgram = gets.chomp
