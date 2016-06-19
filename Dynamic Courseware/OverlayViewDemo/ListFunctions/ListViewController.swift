//
//  OverlayView.swift
//  Dealership
//
//  Created by Sztanyi Szabolcs on 05/01/16.
//  Copyright © 2016 Zappdesigntemplates. All rights reserved.
//

import UIKit


/// Custom view that displays when a user adds a Car to the Garage (Saves it locally)
class ListViewController: UIView {

    var nibValue:String = "ListView"
    
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
    func loadViewFromXibFile(nibCall:String) -> UIView
    {
        let bundle = NSBundle(forClass: self.dynamicType)
        let nib = UINib(nibName: nibCall, bundle: bundle)
        let view = nib.instantiateWithOwner(self, options: nil)[0] as! UIView
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
    func displayView(onView: UIView)
    {
        self.alpha = 1.0
        onView.addSubview(self)

        onView.addConstraint(NSLayoutConstraint(item: self, attribute: .CenterY, relatedBy: .Equal, toItem: onView, attribute: .CenterY, multiplier: 1.0, constant: 0.0)) // move it a bit upwards
        onView.addConstraint(NSLayoutConstraint(item: self, attribute: .CenterX, relatedBy: .Equal, toItem: onView, attribute: .CenterX, multiplier: 1.0, constant: 0.0))
        onView.needsUpdateConstraints()

        // display the view
        transform = CGAffineTransformMakeScale(0.1, 0.1)
        UIView.animateWithDuration(0.3, animations:
            { () -> Void in
                self.alpha = 1.0
                self.transform = CGAffineTransformIdentity
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

        addConstraint(NSLayoutConstraint(item: self, attribute: .Height, relatedBy: .Equal, toItem: nil, attribute: .NotAnAttribute, multiplier: 1.0, constant: 667))
        addConstraint(NSLayoutConstraint(item: self, attribute: .Width, relatedBy: .Equal, toItem: nil, attribute: .NotAnAttribute, multiplier: 1.0, constant: 375))
        addConstraint(NSLayoutConstraint(item: view, attribute: .Top, relatedBy: .Equal, toItem: self, attribute: .Top, multiplier: 1.0, constant: 0.0))
        addConstraint(NSLayoutConstraint(item: view, attribute: .Bottom, relatedBy: .Equal, toItem: self, attribute: .Bottom, multiplier: 1.0, constant: 0.0))
        addConstraint(NSLayoutConstraint(item: view, attribute: .Trailing, relatedBy: .Equal, toItem: self, attribute: .Trailing, multiplier: 1.0, constant: 0.0))
        addConstraint(NSLayoutConstraint(item: view, attribute: .Leading, relatedBy: .Equal, toItem: self, attribute: .Leading, multiplier: 1.0, constant: 0.0))
    }

    /**
     Hides the view with animation
     */
    @IBAction func hideView()
    {
        UIView.animateWithDuration(0.3, animations:
        { () -> Void in
                self.transform = CGAffineTransformMakeScale(0.1, 0.1)
        })
        { (finished) -> Void in
            self.removeFromSuperview()
        }
    }

}
