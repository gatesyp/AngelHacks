//
//  ListViewController.swift
//  Post
//
//  Created by Aron Gates on 06/18/16.
//  Copyright © 2016 geczy.tech All rights reserved.
//

import UIKit

/// Custom view that displays when a user wants to view his analyzed list
class ListViewController: UIView {
    var whichView:String = "ListView"
    var nibValue:String = "ListView"
    
    @IBOutlet var video1: UIWebView!
    @IBOutlet var video2: UIWebView!
    @IBOutlet var video3: UIWebView!
    
    /// Label to show the empty text
    @IBOutlet weak var titleLabel: UILabel!
    /// ImageView that holds the icon
    @IBOutlet weak var emptyIcon: UIImageView!

    // Our custom view from the XIB file
    var view: UIView!

    /// Visual effectView for having a blurry background
    @IBOutlet weak var visualEffectView: UIVisualEffectView!

    /**
     Initialiser method

     - parameter frame: frame to use for the view
     */
    
    override init(frame: CGRect)
    {
        super.init(frame: frame)
        setupView()
    }

    /**
     Initialiser method

     - parameter aDecoder: aDecoder
     */
    required init?(coder aDecoder: NSCoder)
    {
        super.init(coder: aDecoder)
        setupView()
    }
    
    /**
     Loads a view instance from the xib file
     - returns: loaded view
     */
    func loadViewFromXibFile(_ nibCall:String) -> UIView
    {
        let bundle = Bundle(for: self.dynamicType)
        let nib = UINib(nibName: nibCall, bundle: bundle)
        let view = nib.instantiate(withOwner: self, options: nil)[0] as! UIView
        return view
    }

    /**
     Sets up the view by loading it from the xib file and setting its frame
     */
    func setupView()
    {
        let nibCall = nibValue
        view = loadViewFromXibFile(nibCall)
        view.frame = bounds
        view.translatesAutoresizingMaskIntoConstraints = false
        addSubview(view)

        self.translatesAutoresizingMaskIntoConstraints = false

        // saved successfully

        visualEffectView.layer.cornerRadius = 4.0
    }

    /**
     Displays the overlayView on the passed in view

     - parameter onView: the view that will display the overlayView
     */
    func displayView(_ onView: UIView)
    {
        self.alpha = 1.0
        onView.addSubview(self)

        onView.addConstraint(NSLayoutConstraint(item: self, attribute: .centerY, relatedBy: .equal, toItem: onView, attribute: .centerY, multiplier: 1.0, constant: -49.0)) // move it a bit upwards
        onView.addConstraint(NSLayoutConstraint(item: self, attribute: .centerX, relatedBy: .equal, toItem: onView, attribute: .centerX, multiplier: 1.0, constant: 0.0))
        onView.needsUpdateConstraints()

        // display the view
        transform = CGAffineTransform(scaleX: 0.1, y: 0.1)
        UIView.animate(withDuration: 0.3, animations:
            { () -> Void in
                self.alpha = 1.0
                self.transform = CGAffineTransform.identity
            }) { (finished) -> Void in
                /* When finished wait 1.5 seconds, than hide it
                let delayTime = dispatch_time(DISPATCH_TIME_NOW, Int64(1.5 * Double(NSEC_PER_SEC)))
                dispatch_after(delayTime, dispatch_get_main_queue()) {
                    self.hideView()
                }*/
        }
    }

    /**
     Updates constraints for the view. Specifies the height and width for the view
     */
    override func updateConstraints()
    {
        super.updateConstraints()

        addConstraint(NSLayoutConstraint(item: self, attribute: .height, relatedBy: .equal, toItem: nil, attribute: .notAnAttribute, multiplier: 1.0, constant: 618))
        addConstraint(NSLayoutConstraint(item: self, attribute: .width, relatedBy: .equal, toItem: nil, attribute: .notAnAttribute, multiplier: 1.0, constant: 375))
        addConstraint(NSLayoutConstraint(item: view, attribute: .top, relatedBy: .equal, toItem: self, attribute: .top, multiplier: 1.0, constant: 0.0))
        addConstraint(NSLayoutConstraint(item: view, attribute: .bottom, relatedBy: .equal, toItem: self, attribute: .bottom, multiplier: 1.0, constant: 0.0))
        addConstraint(NSLayoutConstraint(item: view, attribute: .trailing, relatedBy: .equal, toItem: self, attribute: .trailing, multiplier: 1.0, constant: 0.0))
        addConstraint(NSLayoutConstraint(item: view, attribute: .leading, relatedBy: .equal, toItem: self, attribute: .leading, multiplier: 1.0, constant: 0.0))
    }

    /**
     Hides the view with animation
     */
    @IBAction func hideView()
    {
        UIView.animate(withDuration: 0.3, animations:
        { () -> Void in
                self.transform = CGAffineTransform(scaleX: 0.1, y: 0.1)
        })
        { (finished) -> Void in
            self.removeFromSuperview()
        }
    }
    
    @IBAction func switchView()
    {
        xibSetupAdvance()
    }
    
    @IBAction func switchViewBack()
    {
        xibSetupBack()
    }
    
    func xibSetupAdvance() {
        view = loadViewFromNibAdvance()
        
        // use bounds not frame or it'll be offset
        view.frame = bounds
        
        // Make the view stretch with containing view
        view.autoresizingMask = [UIViewAutoresizing.flexibleWidth, UIViewAutoresizing.flexibleHeight]
        // Adding custom subview on top of our view (over any custom drawing > see note below)
        
        UIView.animate(withDuration: 0.3, animations:
            { () -> Void in
                self.transform = CGAffineTransform(scaleX: 0.5, y: 1.0)
            })
        { (finished) -> Void in
            self.addSubview(self.view)
            if self.whichView == "ListView3"
            {
                let myURL1 : NSURL = NSURL(string: "https://www.youtube.com/embed/g157qwT1918")!
                let myURLRequest1 : NSURLRequest = NSURLRequest(url: myURL1 as URL)
                let myURL2 : NSURL = NSURL(string: "https://www.youtube.com/embed/9gUdDM6LZGo")!
                let myURLRequest2 : NSURLRequest = NSURLRequest(url: myURL2 as URL)
                let myURL3 : NSURL = NSURL(string: "https://www.youtube.com/embed/zDcf7eEaP0M")!
                let myURLRequest3 : NSURLRequest = NSURLRequest(url: myURL3 as URL)
                self.video1.loadRequest(myURLRequest1 as URLRequest)
                self.video2.loadRequest(myURLRequest2 as URLRequest)
                self.video3.loadRequest(myURLRequest3 as URLRequest)
            }
            UIView.animate(withDuration: 0.3, animations:
                { () -> Void in
                    self.transform = CGAffineTransform(scaleX: 1.0, y: 1.0)
                })
            { (finished) -> Void in
            }
        }
    }
    
    func loadViewFromNibAdvance() -> UIView {
        switch whichView {
        case "ListView":
            whichView = "ListView2"
            break
        case "ListView2":
            whichView = "ListView3"
            break
        default:
            break
        }
        
        let bundle = Bundle(for: self.dynamicType)
        let nib = UINib(nibName: whichView, bundle: bundle)
        let view = nib.instantiate(withOwner: self, options: nil)[0] as! UIView
        
        return view
    }
    
    func xibSetupBack() {
        view = loadViewFromNibBack()
        
        // use bounds not frame or it'll be offset
        view.frame = bounds
        
        // Make the view stretch with containing view
        view.autoresizingMask = [UIViewAutoresizing.flexibleWidth, UIViewAutoresizing.flexibleHeight]
        // Adding custom subview on top of our view (over any custom drawing > see note below)
        
        UIView.animate(withDuration: 0.3, animations:
            { () -> Void in
                self.transform = CGAffineTransform(scaleX: 0.5, y: 1.0)
            })
        { (finished) -> Void in
            self.addSubview(self.view)
            UIView.animate(withDuration: 0.3, animations:
                { () -> Void in
                    self.transform = CGAffineTransform(scaleX: 1.0, y: 1.0)
                })
            { (finished) -> Void in
            }
        }
    }
    
    func loadViewFromNibBack() -> UIView {
        switch whichView {
        case "ListView3":
            whichView = "ListView2"
            break
        case "ListView2":
            whichView = "ListView"
            break
        default:
            break
        }
        
        let bundle = Bundle(for: self.dynamicType)
        let nib = UINib(nibName: whichView, bundle: bundle)
        let view = nib.instantiate(withOwner: self, options: nil)[0] as! UIView
        
        return view
    }
}
