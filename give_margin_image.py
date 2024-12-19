from mergin_giver import margin_giver_writer
import sys


original_dir = sys.argv[1]
copy_dir = sys.argv[2] if len(sys.argv) > 2 else original_dir

give_margin = margin_giver_writer.margin_giver_writer_builder(original_dir)
print("start resizing images")
give_margin(copy_dir)

print("image has resized")