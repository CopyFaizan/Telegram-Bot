<!DOCTYPE html>

<html lang="en" style="height: 100%">
    <head>
        <meta charset="utf-8">
        <title>03_voice_chatbot.py : /home/Faizan9393/03_voice_chatbot.py : Editor : Faizan9393 : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="03_voice_chatbot.py : /home/Faizan9393/03_voice_chatbot.py : Editor : Faizan9393 : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" />

        <link rel="stylesheet" href="/static/CACHE/css/output.ff34947502d6.css" type="text/css" media="screen">
        <link rel="stylesheet" href="/static/CACHE/css/output.b9a4961a16f7.css" type="text/css"><link rel="stylesheet" href="/static/CACHE/css/output.135dadead6d9.css" type="text/css" media="screen">

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "K3EEnB7n0I4nvkwzwNUixt8yqJtqRaOu6nV8bTwQlRHTbs4KgwJBWCgzZXttLNzD";
        </script>
        <script src="/static/CACHE/js/output.9912b9c89b96.js"></script>
        

        <script src="/static/CACHE/js/output.ce8d62eca661.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Faizan9393/files/home/Faizan9393/03_voice_chatbot.py",
          check_hash: "/user/Faizan9393/files/home/Faizan9393/03_voice_chatbot.py",
          update_editor_mode_preference: "/user/Faizan9393/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Faizan9393/consoles/",
        });
        var filename = "/home/Faizan9393/03_voice_chatbot.py";
        var hash = "7dd6985ec0d75566044d46e577bacaf0";
        var interpreter = "python3.10";

        
            Anywhere.Editor.InitializeAce(ace, Anywhere.urls, filename, hash, interpreter, "pythonanywhere.com");
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/Faizan9393/files/sharing/",
            csrfToken: "K3EEnB7n0I4nvkwzwNUixt8yqJtqRaOu6nV8bTwQlRHTbs4KgwJBWCgzZXttLNzD",
            path: "/home/Faizan9393/03_voice_chatbot.py"
          }
        );

      });
    </script>

        

    </head>

     <body style="height:100%;">
       <div style="min-height: 100%; position: relative;">
        
        
  




  <nav class="navbar navbar-default fullscreen-main-navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">
        <img id="id_logo" src="/static/anywhere/images/PA-logo-snake-only.svg" height="100%" />
      </a>
    </div>

    <div class="extra-nav-content">
      

  <div id="id_editor_toolbar">

    <div class="pull-left">
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Faizan9393/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Faizan9393/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Faizan9393/files/home/Faizan9393" target="_parent">Faizan9393</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">03_voice_chatbot.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
    </div>

    <div id="id_editor_messages" class="pull-left">
      

    </div>

    <div class="pull-right">
      <div id="id_editor_buttons_right" class="form-inline">
        <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
        <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
        
          <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
          <select id="id_keybinding_mode_select" class="form-control input-sm">
            <option value="normal">Normal</option>
            <option value="vim">Vim</option>
          </select>
        
        <button id="id_display_sharing_options" class="btn btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
          <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
          Share
        </button>
        
          <button id="id_save" class="btn btn-success" title="Save (Ctrl + S)">
            <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
            Save
          </button>
          <button id="id_save_as" class="btn btn-default" title="Save As">Save as...</button>
        
        
          <button class="btn btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
        

        
          
        
      </div>
    </div>

  </div>


    </div>

    <div class="dropdown fullscreen-hamburger fullscreen-mini-nav">
      <button type="button" class="navbar-toggle" data-toggle="dropdown"  role="button" aria-haspopup="true" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <ul class="dropdown-menu pull-right">
        
  <li class=""><a id="id_dashboard_link" href="/user/Faizan9393/">Dashboard</a></li>
  <li class=""><a id="id_consoles_link" href="/user/Faizan9393/consoles/">Consoles</a></li>
  <li class=""><a id="id_files_link" href="/user/Faizan9393/files/home/Faizan9393">Files</a></li>
  <li class=""><a id="id_web_app_link" href="/user/Faizan9393/webapps/">Web</a></li>
  <li class=""><a id="id_tasks_link" href="/user/Faizan9393/tasks_tab/">Tasks</a></li>
  <li class=""><a id="id_databases_link" href="/user/Faizan9393/databases/">Databases</a></li>


        
<li class=""><a href="" target="_parent" class="feedback_link">Send feedback</a></li>


<li class=""><a href="/forums/" target="_parent" class="forums_link">Forums</a></li>
<li class=""><a href="https://help.pythonanywhere.com/" target="_parent" class="help_link">Help</a></li>
<li class=""><a href="https://blog.pythonanywhere.com/" target="_parent" class="blog_link">Blog</a></li>

  
  <li class=""><a href="/user/Faizan9393/account/" target="_parent" class="account_link">Account</a></li>
  <li class="">
    <form action="/logout/" method="POST" target="_parent">
      <input type="hidden" name="csrfmiddlewaretoken" value="K3EEnB7n0I4nvkwzwNUixt8yqJtqRaOu6nV8bTwQlRHTbs4KgwJBWCgzZXttLNzD">
      <button type="submit" class="btn-link logout_link">Log out</button>
    </form>
  </li>


      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">from telegram.ext import Updater, MessageHandler, Filters
import telegram
import openai
from moviepy.editor import AudioFileClip
import time

openai.api_key = &quot;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&quot;
TELEGRAM_API_TOKEN = &quot;6053527307:AAFMF-q9MVJkFoNXh4zmdPdXiqCRHe3NYK0&quot;

messages = [{&quot;role&quot;: &quot;assistant&quot;, &quot;content&quot;: &quot;Become Chatgpt&quot;}]

def text_message(update, context):
    messages.append({&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: update.message.text})
    response = openai.ChatCompletion.create(
        model=&quot;gpt-3.5-turbo&quot;,
        messages=messages
    )
    ChatGPT_reply = response[&quot;choices&quot;][0][&quot;message&quot;][&quot;content&quot;]
    update.message.reply_text(text=f&quot;*[Bot]:* {ChatGPT_reply}&quot;, parse_mode=telegram.ParseMode.MARKDOWN)
    messages.append({&quot;role&quot;: &quot;assistant&quot;, &quot;content&quot;: ChatGPT_reply})

def voice_message(update, context):
    update.message.reply_text(&quot;I&#39;ve received a voice message! Please give me a second to respond :)&quot;)
    voice_file = context.bot.getFile(update.message.voice.file_id)
    voice_file.download(&quot;voice_message.ogg&quot;)
    audio_clip = AudioFileClip(&quot;voice_message.ogg&quot;)
    audio_clip.write_audiofile(&quot;voice_message.mp3&quot;)
    audio_file = open(&quot;voice_message.mp3&quot;, &quot;rb&quot;)
    transcript = openai.Audio.transcribe(&quot;whisper-1&quot;, audio_file).text
    update.message.reply_text(text=f&quot;*[You]:* _{transcript}_&quot;, parse_mode=telegram.ParseMode.MARKDOWN)
    messages.append({&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: transcript})
    response = openai.ChatCompletion.create(
        model=&quot;gpt-3.5-turbo&quot;,
        messages=messages
    )
    ChatGPT_reply = response[&quot;choices&quot;][0][&quot;message&quot;][&quot;content&quot;]
    update.message.reply_text(text=f&quot;*[Bot]:* {ChatGPT_reply}&quot;, parse_mode=telegram.ParseMode.MARKDOWN)
    messages.append({&quot;role&quot;: &quot;assistant&quot;, &quot;content&quot;: ChatGPT_reply})

def start_timer(duration):
    if &quot;for&quot; in duration:
        # Extract the duration from the phrase
        duration = int(duration.split(&quot; &quot;)[4].split(&quot;-&quot;)[0])

        # Start the timer
        print(f&quot;Starting the timer for {duration} minutes.&quot;)
        time.sleep(duration * 60)
        print(&quot;Timer is up!&quot;)

updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text &amp; (~Filters.command), text_message))
dispatcher.add_handler(MessageHandler(Filters.voice, voice_message))
updater.start_polling()
updater.idle()</div>
      

      <div id="id_ide_console">
        
          <iframe src="/user/Faizan9393/consoles/29205737/frame/" id="id_console" name="console" class="soft_keyboard_sensitive">
          </iframe>
        
      </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
      <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
      <div class="dialog_buttons">
        <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
        <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
      </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
      <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
      <div class="dialog_buttons">
        <button id="id_force_save" class="btn btn-danger">Force Save</button>
        <button id="id_cancel_save" class="btn btn-default">Cancel</button>
      </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
      <form class="form-inline">
        <div class="form-group">
          <label for="id_save_as_path">Please enter a path:</label>
          <input id="id_save_as_path" class="form-control" style="width: 100%;" />
        </div>
        <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
        <p>
          <span id="id_save_as_error" class="error_message"></span>
        </p>
        <div class="dialog_buttons">
          <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
          <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
        </div>
      </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>


        
      </div>

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" style="display: none">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_rate_limit_error" style="display: none">
        Sorry, we have had to rate-limit your feedback sending.<br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_success" style="display: none">
        Thanks for the feedback! Our tireless devs will get back to you soon.
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
    <div id="id_feedback_dialog_only_close_button" style="display: none">
        <button class="btn btn-primary" id="id_feedback_dialog_close_button">Close</button>
    </div>
</div>


        
            <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-18014859-6', 'auto');
                ga('send', 'pageview');
            </script>
        

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
