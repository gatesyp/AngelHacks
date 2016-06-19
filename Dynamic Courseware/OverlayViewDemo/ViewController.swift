//
//  ViewController.swift
//  Dynamic Coursewear
//
//  Created by Aron Gates on 06-18-16.
//  Copyright © 2016 geczy.tech All rights reserved.
//

import UIKit

class ViewController: UIViewController
{
    @IBOutlet var listButton: UIButton!
    @IBOutlet var recordButton: UIButton!
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
    }
    override func didReceiveMemoryWarning()
    {
        super.didReceiveMemoryWarning()
    }
    
    // Overlay Record
    lazy var recordView: RecordViewController = {
        let recordView = RecordViewController()
        return recordView
    }()
    
    // Overlay List
    lazy var listView: ListViewController = {
        let listView = ListViewController()
        return listView
    }()
    
    @IBAction func recordViewPress()
    {
        recordView.displayView(view)
    }
    
    @IBAction func listViewPress()
    {
        listView.displayView(view)
    }

}

