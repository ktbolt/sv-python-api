'''
Test the sv.geometry.LoftNurbsOptions() class. 
'''
import sv

loft_nurbs_options = sv.geometry.LoftNurbsOptions()
print(dir(loft_nurbs_options))
print("loft_nurbs_options.u_knot_span_type: " + str(loft_nurbs_options.u_knot_span_type))

loft_nurbs_options.u_knot_span_type = "fred";
print("loft_nurbs_options.u_knot_span_type: " + str(loft_nurbs_options.u_knot_span_type))

