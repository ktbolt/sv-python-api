
import os
import glob
import collections

class ProjectPluginNames(object):
    IMAGES = "Images"
    MESHES = "Meshes"
    MODELS = "Models"
    PATHS = "Paths"
    SEGMENTATIONS = "Segmentations"
    SIMULATIONS = "Simulations"
    names = [ IMAGES, MESHES, MODELS, PATHS, SEGMENTATIONS, SIMULATIONS ]

class ProjectPluginInstance(object):
    def __init__(self, name, file_name):
        self.name = name 
        self.file_name = file_name 

class ProjectPlugin(object):
    def __init__(self, name):
        self.name = name 
        self.instances = None
        self.file_extension = None

    def get_files(self, project_dir):
        ''' Get the names of the files defined for each plugin.
        '''
        #print("[ProjectPlugin.read_files] Plugin directory: {0:s}".format(self.name))
        #print("[ProjectPlugin.read_files]   File extension: {0:s}".format(self.file_extension))
        rep = project_dir+"/"+self.name+"/*."+self.file_extension
        pfiles = [f for f in glob.glob(rep)]
        #print("[ProjectPlugin.read_files] Files: {0:s}".format(str(files)))
        if len(pfiles) > 0:
            self.instances = []
        for pfile in pfiles:
            base = os.path.basename(pfile)
            name = os.path.splitext(base)[0]
            #print("[ProjectPlugin.read_files]   Instance: {0:s}".format(str(name)))
            self.instances.append( ProjectPluginInstance(name, pfile) )

    def get_plugin_instances(self):
        return ', '.join([inst.name for inst in self.instances]) 

class ProjectImagesPlugin(ProjectPlugin):
    def __init__(self):
        super().__init__(ProjectPluginNames.IMAGES)
        self.file_extension = 'vti'

class ProjectMeshesPlugin(ProjectPlugin):
    def __init__(self):
        super().__init__(ProjectPluginNames.MESHES)
        self.file_extension = 'msh'

class ProjectModelsPlugin(ProjectPlugin):
    def __init__(self):
        super().__init__(ProjectPluginNames.MODELS)
        self.file_extension = 'mdl'

class ProjectPathsPlugin(ProjectPlugin):
    def __init__(self):
        super().__init__(ProjectPluginNames.PATHS)
        self.file_extension = 'pth'

    def get_path(self, name):
        print("[ProjectPathsPlugin.get_path] Name: {0:s}".format(name))
        instance = None
        for inst in self.instances:
            if name == inst.name:
                instance = inst
        if instance == None:
            print("[ProjectPathsPlugin.get_path] ERROR: Name {0:s} not found.".format(name))
            return None

class ProjectSegmentationsPlugin(ProjectPlugin):
    def __init__(self):
        super().__init__(ProjectPluginNames.SEGMENTATIONS)
        self.file_extension = 'ctgr'

class ProjectSimulationsPlugin(ProjectPlugin):
    def __init__(self):
        super().__init__(ProjectPluginNames.SIMULATIONS)
        self.file_extension = 'sjb'

class Project(object):
    ''' 
    This class is used to store an SV project. 
    '''
    def __init__(self):
        self.project_dir = None
        self.add_plugins()

    def add_plugins(self):
        self.plugins = collections.OrderedDict()
        self.plugins[ProjectPluginNames.IMAGES] = ProjectImagesPlugin()
        self.plugins[ProjectPluginNames.MESHES] = ProjectMeshesPlugin()
        self.plugins[ProjectPluginNames.MODELS] = ProjectModelsPlugin()
        self.plugins[ProjectPluginNames.PATHS] = ProjectPathsPlugin()
        self.plugins[ProjectPluginNames.SEGMENTATIONS] = ProjectSegmentationsPlugin()
        self.plugins[ProjectPluginNames.SIMULATIONS] = ProjectSimulationsPlugin()
        '''
        for name,plugin in self.plugins.items():
            print("Plugin name: {0:s}".format(name))
            print("       name: {0:s}".format(plugin.name))
        '''

    def open(self, project_dir):
        print("[Project.open] Project directory: {0:s}".format(project_dir))
        self.project_dir = project_dir 
        for name,plugin in self.plugins.items():
            plugin.get_files(project_dir)

    def get_project_plugin_instances(self):
        plugin_instances = collections.OrderedDict()
        for name,plugin in self.plugins.items():
            plugin_instances[name] =  plugin.get_plugin_instances()
        return plugin_instances

    def get_path(self, name):
        self.plugins[ProjectPluginNames.PATHS].get_path(name)


