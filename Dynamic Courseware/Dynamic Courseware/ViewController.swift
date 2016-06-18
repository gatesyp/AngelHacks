//
//  ViewController.swift
//  Dynamic Courseware
//
//  Created by Aron Gates on 6/18/16.
//  Copyright © 2016 Gates. All rights reserved.
//

import UIKit

class ViewController: UIViewController//, AudioRecorderViewControllerDelegate
{
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning()
    {
        super.didReceiveMemoryWarning()
        
        // Dispose of any resources that can be recreated.
    }
    
    
    @IBAction func doPlayAction(sender: AnyObject)
    {
        //let controller = AudioRecorderViewController()
        //controller.audioRecorderDelegate = self
        //presentViewController(controller, animated: true, completion: nil)
    }
    
    func audioRecorderViewControllerDismissed(withFileURL fileURL: NSURL?)
    {
        // do something with fileURL
        // dismissViewControllerAnimated(true, completion: nil)
    }
    
    
}