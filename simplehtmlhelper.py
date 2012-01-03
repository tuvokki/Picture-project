title = "Test desktop show"
slogan = "Some nice slides"
slug = "a. photo"
def printli (dir, filename):
  print """
  <li><!--printli -->
    <a class="thumb" name="leaf" href="%(dir)s/low/%(filename)s" title="%(filename)s">
      <img src="%(dir)s/thumbs/%(filename)s" alt="%(filename)s" />
    </a>
    <div class="caption">
      <div class="download">
        <a href="%(dir)s/full/%(filename)s">Download Original</a>
      </div>
      <div class="image-title">Title %(filename)s</div>
      <div class="image-desc">Test Desktop</div>
    </div>
  </li>
  """ % {'dir' : dir, 'filename' : filename}

def printline(line):
  print "<h3>%(line)s</h3>" % {'line':line}

def header ():
	print "Content-type: text/html"
	print """
  <html>
  	<head>
  		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
  		<title>%(title)s</title>
  		<link rel="stylesheet" href="css/basic.css" type="text/css" />
  		<link rel="stylesheet" href="css/galleriffic-2.css" type="text/css" />
  		<script type="text/javascript" src="js/jquery-1.3.2.js"></script>
  		<script type="text/javascript" src="js/jquery.galleriffic.js"></script>
  		<script type="text/javascript" src="js/jquery.opacityrollover.js"></script>
  		<!-- We only want the thunbnails to display when javascript is disabled -->
  		<script type="text/javascript">
  			document.write('<style>.noscript { display: none; }</style>');
  		</script>
  	</head>
  	<body>
  		<div id="page">
  			<div id="container">
  				<h1><a href="/">%(slogan)s</a></h1>
          <h2>%(slug)s</h2>

  				<!-- Start Advanced Gallery Html Containers -->
  				<div id="gallery" class="content">
  					<div id="controls" class="controls"></div>
  					<div class="slideshow-container">
  						<div id="loading" class="loader"></div>
  						<div id="slideshow" class="slideshow"></div>
  					</div>
  					<div id="caption" class="caption-container"></div>
  				</div>
  				<div id="thumbs" class="navigation">
  					<ul class="thumbs noscript">
	""" % {'title' : title, 'slogan' : slogan, "slug" : slug}

def footer ():
	print """

  					</ul>
  				</div>
  				<div style="clear: both;"></div>
  			</div>
  		</div>
  		<div id="footer">Design &copy; 2009 Trent Foley</div>
  		<script type="text/javascript">
  			jQuery(document).ready(function($) {
  				// We only want these styles applied when javascript is enabled
  				$('div.navigation').css({'width' : '300px', 'float' : 'left'});
  				$('div.content').css('display', 'block');

  				// Initially set opacity on thumbs and add
  				// additional styling for hover effect on thumbs
  				var onMouseOutOpacity = 0.67;
  				$('#thumbs ul.thumbs li').opacityrollover({
  					mouseOutOpacity:   onMouseOutOpacity,
  					mouseOverOpacity:  1.0,
  					fadeSpeed:         'fast',
  					exemptionSelector: '.selected'
  				});

  				// Initialize Advanced Galleriffic Gallery
  				var gallery = $('#thumbs').galleriffic({
  					delay:                     2500,
  					numThumbs:                 15,
  					preloadAhead:              10,
  					enableTopPager:            true,
  					enableBottomPager:         true,
  					maxPagesToShow:            7,
  					imageContainerSel:         '#slideshow',
  					controlsContainerSel:      '#controls',
  					captionContainerSel:       '#caption',
  					loadingContainerSel:       '#loading',
  					renderSSControls:          true,
  					renderNavControls:         true,
  					playLinkText:              'Play Slideshow',
  					pauseLinkText:             'Pause Slideshow',
  					prevLinkText:              '&lsaquo; Previous Photo',
  					nextLinkText:              'Next Photo &rsaquo;',
  					nextPageLinkText:          'Next &rsaquo;',
  					prevPageLinkText:          '&lsaquo; Prev',
  					enableHistory:             false,
  					autoStart:                 false,
  					syncTransitions:           true,
  					defaultTransitionDuration: 900,
  					onSlideChange:             function(prevIndex, nextIndex) {
  						// 'this' refers to the gallery, which is an extension of $('#thumbs')
  						this.find('ul.thumbs').children()
  							.eq(prevIndex).fadeTo('fast', onMouseOutOpacity).end()
  							.eq(nextIndex).fadeTo('fast', 1.0);
  					},
  					onPageTransitionOut:       function(callback) {
  						this.fadeTo('fast', 0.0, callback);
  					},
  					onPageTransitionIn:        function() {
  						this.fadeTo('fast', 1.0);
  					}
  				});
  			});
  		</script>
  	</body>
  </html>
	""" 
