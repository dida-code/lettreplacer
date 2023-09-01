pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'lettreplacer')
gnome = import('gnome')

gnome.compile_resources('lettreplacer',
  'lettreplacer.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'lettreplacer.in',
  output: 'lettreplacer',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x'
)

lettreplacer_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'txt.png',
]

install_data(lettreplacer_sources, install_dir: moduledir)
